from django.urls import path
from . import views

urlpatterns = [
    path('', views.aggregate_home, name='aggregate_home'),
    path('predict_home', views.predictive_home, name='predict_home'),
    path('predict', views.predict, name='predict'),
    path('aggregate', views.aggregate, name='aggregate'),
]
