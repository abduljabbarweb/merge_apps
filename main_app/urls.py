from django.urls import path, include
from . import views

# from merg_apps import app_1, app_2

urlpatterns = [
    path('', views.home, name = 'home'),
    path('app2', include('app_2.urls')),
    #path('app2/', include('app_2.urls')),
]