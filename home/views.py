from django.contrib.postgres.search import TrigramSimilarity
from django.db.models.functions import Greatest
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from home.models import Feedback
from museum.models import Museum
from news.models import News
from books.models import Book, CategoryBook
from events.models import Event
from itertools import chain


def home(request):
    return render(request, 'home/index.html')


def feedback(request):
    if request.is_ajax():
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        user_feedback = Feedback.objects.create(
            name=name,
            email=email,
            message=message
        )

        user_feedback.save()
        if user_feedback is not None:
            return JsonResponse({'status': True})
        else:
            return JsonResponse({'status': False})
    return redirect('home:index')


def search(request):
    context = {}
    if request.method == 'GET':
        keywords = request.GET.get('keywords')

        if keywords is not None:
            # News list
            news_results = News.published.annotate(
                similarity=Greatest(
                    TrigramSimilarity('title', keywords),
                    TrigramSimilarity('description', keywords),
                    TrigramSimilarity('body', keywords),
                )
            ).filter(similarity__gt=0.1).order_by('-similarity')

            # Books list
            book_results = Book.objects.annotate(
                similarity=Greatest(
                    TrigramSimilarity('name', keywords),
                    TrigramSimilarity('body', keywords),
                    TrigramSimilarity('author', keywords),
                )
            ).filter(active=True).filter(similarity__gt=0.1).order_by('-similarity')

            # Events list
            events_result = Event.active.annotate(
                similarity=Greatest(
                    TrigramSimilarity('title', keywords),
                    TrigramSimilarity('description', keywords),
                    TrigramSimilarity('place', keywords),
                    TrigramSimilarity('author', keywords),
                )
            ).filter(similarity__gt=0.1).order_by('-similarity')

            # Museum list
            museum_result = Museum.published.annotate(
                similarity=TrigramSimilarity('title', keywords)
            ).filter(gallery=True).filter(similarity__gt=0.1).order_by('-similarity')

            # Combine querysets
            queryset_chain = chain(
                news_results,
                book_results,
                events_result,
                museum_result
            )

            qs = sorted(queryset_chain,
                        key=lambda instance: instance.pk,
                        reverse=True)

            context = {
                'queryset_list': qs,
                'keywords': keywords,
                'founded': len(qs)
            }
    return render(request, 'search/search.html', context)
