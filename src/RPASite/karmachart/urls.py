import sys, os
from django.urls import path
from . import views

app_name = 'karmachart'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('',views.IndexView.collect_data,name='collect_data'),
    path('clear_session', views.IndexView.clear_sesh, name='clear_sesh')
]