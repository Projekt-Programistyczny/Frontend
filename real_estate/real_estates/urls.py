
"""
Definiuje wzorce adresów URL dla real_estates.
"""

from django.urls import re_path
from . import views
urlpatterns = [
    # Strona główna.
    re_path(r'^$', views.index, name="index"),
    # Wyświetlanie wszytskich ogłoszeń.
    re_path(r'^announcement/$', views.announcement, name="announcement"),
]

