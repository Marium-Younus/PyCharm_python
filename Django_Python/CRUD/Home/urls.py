
from django.urls import path
from . import views

urlpatterns = [
    path('',views.func_home),
    path('showrecord', views.func_show),
    path('senddata', views.func_save),
    path('delete', views.func_delete),
    path('edit', views.func_edit),
    path('recordEdit', views.update_record)
]
