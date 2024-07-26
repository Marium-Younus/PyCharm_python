from django.urls import path,include
from . import views
urlpatterns = [

    path('',views.index),
    path('h',views.home),
    path('b',views.book),
    path('v',views.video),
    path('r',views.registration),
    path('l',views.login),
    path('c',views.contact),
    path('logout', views.funct_logout),
    path('datains',views.funct_save)

]