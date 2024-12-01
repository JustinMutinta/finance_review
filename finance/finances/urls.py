from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('year/<str:pk>', views.year, name='year'),
    path('year/<str:year>/<str:month>', views.month, name='month'),
    path('expense/<str:pk>', views.expense, name='expense'),
    path('index', views.index, name='index'),

]