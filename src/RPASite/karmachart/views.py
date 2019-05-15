from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
import requests
from django.views import generic
from .models import Job
from .forms import NameForm, HomeForm
import Reddit.data_collection


def collect_data(request):

    Reddit.data_collection.collect_submission_ids('flying', 'top',5)
    return render(request,'karmachart/index.html')



class IndexView(generic.ListView):
    template_name = 'karmachart/index.html'

    def get_queryset(self):
        """Return the last five published questions."""
        return 'testing'
    
    def get(self, request):
        form = HomeForm()
        return render(request,self.template_name,{'form': form})

    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            subreddit = form.cleaned_data['subreddit']
            sort_by = form.cleaned_data['sort_by']
            limit = form.cleaned_data['limit']
            Reddit.data_collection.collect_submission_ids(subreddit,sort_by,limit)

        args = {'form': form,'subreddit': subreddit}
        return render(request, self.template_name, args)






