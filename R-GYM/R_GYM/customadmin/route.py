from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.dashboard),
    path('login', views.login),
    path('product', views.product),
    path('admin-packages', views.packages),
    path('admin-trainer', views.trainer),
    path('add-class', views.add_class),
    path('admin-time-table', views.time_table),
    path('pending-order', views.pending_order),
    path('completed-order', views.completed_order),
    path('admin-contact', views.contact),
    # ============== Ajax
    path('add-category', views.cat),
    path('add-product', views.pro),
    path('add-package', views.pack),
    path('add-trainer', views.train),
    path('add-class-data', views.class_data),
    path('add-time-table', views.add_time_tale),
    path('order-completed', views.order_completed),
]