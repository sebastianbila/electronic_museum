from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView

from events.models import Event, EventSubscribers


class EventListView(ListView):
    model = Event
    template_name = 'events/events.html'  # Default: <app_label>/<model_name>_list.html
    context_object_name = 'events'  # Default: object_list
    paginate_by = 9
    queryset = Event.active.all()  # Default: Model.objects.all()


def event_detail(request, event, pk):
    event = get_object_or_404(Event,
                              id=pk,
                              slug=event,
                              status='active')

    sub_status = False
    user = request.user
    if user is not None and not user.is_anonymous:
        if EventSubscribers.objects.filter(user=user).exists():
            sub_status = True

    context = {
        'event': event,
        'sub_status': sub_status
    }
    return render(request, 'events/event_single.html', context)


def subscribe(request):
    if request.is_ajax():
        pk = request.POST['id']
        user = request.user
        event = get_object_or_404(Event,
                                  id=pk,
                                  status='active')

        if user is not None:
            if EventSubscribers.objects.filter(user=user).exists():
                print('User already subscribed')
                return JsonResponse({'status': False})
            else:
                model = EventSubscribers.objects.create(
                    event=event,
                    user=user
                )
                model.save()
                if model:
                    return JsonResponse({'status': True})
                else:
                    return JsonResponse({'status': False})
    return redirect('events:home')


def unsubscribe(request):
    if request.is_ajax():
        user = request.user

        if user is not None:
            subs = EventSubscribers.objects.get(user=user)
            if subs:
                subs.delete()
                return JsonResponse({'status': True})
            else:
                return JsonResponse({'status': False})
        else:
            return JsonResponse({'status': False})
    return redirect('events:home')
