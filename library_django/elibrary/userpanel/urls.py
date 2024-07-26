from django.urls import path

from .views import video
from . import views
urlpatterns =[
    path('', video),
    path('search/',views.searchBar,name='search')
]