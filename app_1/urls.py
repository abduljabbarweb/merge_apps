from django.urls import path, include
from . import views
#from merg_apps import app_1, app_2

urlpatterns = [
    path('', views.home, name = 'home'),

]