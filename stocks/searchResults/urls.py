from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='searchResultsindex'),
    #path('graphs/(?P<stockname>\w{0,50})/$', views.i2, name='graphs'),
    #path('graphs/gp/(?P<stockcode>w{0,50})', views.gp, name='gp')
]