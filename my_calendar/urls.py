from django.urls import path

from . import views

urlpatterns = [
    path('events/new/', views.NewEvent.as_view(), name='new_event'),
    path('', views.EventsList.as_view(), name='index'),
]
