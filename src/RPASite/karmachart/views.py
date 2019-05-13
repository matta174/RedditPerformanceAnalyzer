from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
import requests
from django.views import generic
from .models import Job
import Reddit.data_collection

def collect_data(request):
    Reddit.data_collection.collect_submission_ids('flying', 'top',5)
    return render(request,'karmachart/index.html')

class IndexView(generic.ListView):
    template_name = 'karmachart/index.html'

    def get_queryset(self):
        """Return the last five published questions."""
        return 'testing'





