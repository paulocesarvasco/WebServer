from django.contrib import admin
from django.urls import path
from server import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('messages/', views.allMessages),
    path('messages/<int:pk>', views.getMessage),
    path('messages/edit/<int:pk>', views.editMessage),
    path('messages/delete/<int:pk>', views.deleteMessage),
    path('messages/post', views.registerMessage),
]
