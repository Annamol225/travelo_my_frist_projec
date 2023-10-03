from django.urls import path

from travelapp import views


urlpatterns = [
    path('', views.fun, name='fun'),
    path('add', views.add, name='add'),
]