from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('tvs/', include('tvs.urls')),
    path('admin/', admin.site.urls),
]