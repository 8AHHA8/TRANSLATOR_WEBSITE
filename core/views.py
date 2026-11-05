from django.shortcuts import render, get_object_or_404
from .models import Page, Service


def index(request):
    context = {
        'services': Service.objects.all(),
        'pages': Page.objects.filter(show_in_menu=True),
    }
    return render(request, 'core/index.html', context)


def page_detail(request, slug):
    page = get_object_or_404(Page, slug=slug)
    return render(request, 'core/page.html', {'page': page})