from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='graphs'),
    path('gp/', views.gp, name='gp')
]