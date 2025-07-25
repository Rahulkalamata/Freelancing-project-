from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('predict/', views.budget_prediction, name='budget_prediction'),
]
