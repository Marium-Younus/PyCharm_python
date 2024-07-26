from django.contrib import admin
from django.urls import path,include
from userpanel import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('userpanel.route')),
    path('l/', views.login, name='login'),
    path('h', views.home, name='home'),
    path('v/',views.video ,name='video'),
    path('',include('userpanel.urls'))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
