from django.contrib import admin
from django.urls import include, path
from server import views

urlpatterns = [
    path('server/', include('server.urls')),
    path('admin/', admin.site.urls),
    path('all', views.allMessages, name='all'),
]
