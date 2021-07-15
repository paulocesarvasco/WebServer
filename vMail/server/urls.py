from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all', views.allMessages, name='all'),
    path('<int:MessageID>/', views.messageDetails, name='details'),
]
