from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from taggit.models import Tag

from news.models import News, Comment


def news_list(request, tag_slug=None):
    object_list = News.published.all()

    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])

    paginator = Paginator(object_list, 9)  # 9 posts in each page
    page = request.GET.get('page')

    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        news = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        news = paginator.page(paginator.num_pages)

    context = {
        'page': page,
        'news': news,
        'tag': tag
    }

    return render(request, 'news/news.html', context)


def news_detail(request, news, pk):
    news = get_object_or_404(News,
                             id=pk,
                             slug=news,
                             status='published')

    # List of active comments
    comments = news.comments.filter(active=True).order_by('-created')

    if request.method == 'POST':
        # A comment was posted
        message = request.POST['message']
        new_comment = Comment.objects.create(
            news=news,
            username=request.user.username,
            email=request.user.email,
            body=message
        )
        new_comment.save()
        return redirect(news.get_absolute_url())

    context = {
        'news': news,
        'comments': comments,
    }
    return render(request, 'news/single_news.html', context)
