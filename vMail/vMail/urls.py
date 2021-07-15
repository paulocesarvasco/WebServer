from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('server/', include('server.urls')),
    path('admin/', admin.site.urls),
]
