from django.shortcuts import render

# Create your views here.
from .models import RealEstates, Links
from django.db.models import F


def index(request):
    """Strona główna dla aplikacji Real Estate."""
    announcement = RealEstates.objects.exclude(price=-1, rent=-1, rooms=-1, type="Failed", status="Failed")[:100].all()
    context = {'announcement': announcement}

    return render(request, 'real_estates/index.html' , context)

def announcement(request):
    """Wyświetlanie wszytskich ogłoszeń."""
    #announcement = RealEstates.objects.select_related("link").all()[:100]
    announcement = RealEstates.objects.exclude(price=-1, rent=-1, rooms=-1, type="Failed", status="Failed")[:100].all()
    #announcement = RealEstates.objects.annotate(Links__url=F('RealEstates__url'))
    #announcement = RealEstates.objects.extra(
     #   select={
      #      'links':
       #         'SELECT city_name FROM Links WHERE Links.url = RealEstates.url'
        #}
    #)
    context = {'announcement': announcement}
    return render(request, 'real_estates/announcement.html', context)

