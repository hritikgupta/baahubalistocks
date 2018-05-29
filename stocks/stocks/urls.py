from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('search/',include('searchResults.urls')),
    path('graph/', include('grapher.urls')),
    path('predict/', include('top3.urls')),
    path('result/', include('result.urls')),
]
