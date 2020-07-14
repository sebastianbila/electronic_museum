from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView

from museum.models import Museum


class MuseumListView(ListView):
    model = Museum
    template_name = 'museum/museum_list.html'  # Default: <app_label>/<model_name>_list.html
    context_object_name = 'museum'  # Default: object_list
    paginate_by = 9
    queryset = Museum.published.all()  # Default: Model.objects.all()


def gallery(request, museum_item, pk):
    museum_item = get_object_or_404(Museum,
                                    id=pk,
                                    slug=museum_item,
                                    active=True)

    # List of gallery
    gallery_item = museum_item.gallery.filter(active=True)

    context = {
        'museum': museum_item,
        'gallery': gallery_item
    }
    return render(request, 'museum/gallery.html', context)


