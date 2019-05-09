from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Job
import Reddit.data_collection


class IndexView(generic.ListView):
    template_name = 'karmachart/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return 'testing'

    def collect_data(self):
        Reddit.data_collection.collect_submission_ids('flying', 'top',5)
        return 'blank'
    # def add_job(self):
    def clear_sesh(self,request):
        print('SESSION CLEARED')
        return 'test'

