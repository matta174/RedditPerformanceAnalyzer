import sys, os
from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'karmachart'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('trackdata', views.TrackDataView.as_view(),name='track_data'),
    url(r'^$',views.IndexView.as_view(),name='index')
    # url(r'^collect_data',views.collect_data,name='collect_data')
]