from csv import DictReader

from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    with open(settings.BUS_STATION_CSV, encoding='UTF-8') as file:
        reader = list(DictReader(file))

    paginator = Paginator(reader, 10)
    num_page = int(request.GET.get('page', 1))
    page = paginator.get_page(num_page)

    context = {
        'bus_stations': page.object_list,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
