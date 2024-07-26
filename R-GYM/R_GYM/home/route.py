from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('classes', views.classes),
    path('classes-single', views.classes_single),
    path('classes-timetable', views.classes_timetable),
    path('our-trainers', views.our_trainers),
    path('trainers-single', views.trainers_single),
    path('services', views.services),
    path('contact-us', views.contact_us),
    path('gallery', views.gallery),
    path('gallery-single', views.gallery_single),
    path('shop', views.shop),
    path('shop-single', views.shop_single),
    path('shop-checkout', views.shop_checkout),

    path('thank-you', views.thank_you),
]