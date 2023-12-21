from django.urls import path
from django.conf.urls.static import static
from . import views
from taskmanager import settings

urlpatterns = [
     path('', views.index, name='home'),
     path('about-us', views.about, name='about'),
     path('create', views.create, name='create'),
     path('tov', views.tov, name='tov')

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)