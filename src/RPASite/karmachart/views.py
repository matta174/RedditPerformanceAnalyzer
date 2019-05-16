from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
import requests
from django.views import generic
from .models import Job, BatchIds
from .forms import NameForm, DataForm
import Reddit.data_collection


class IndexView(generic.ListView):
    template_name = 'karmachart/index.html'
    batchids = Reddit.data_collection.database_interactions.get_all_batchIds_from_db()
    

    def get_queryset(self):
        """Return the last five published questions."""
        return BatchIds.objects.order_by('-pub_date')[:5]
    
    # def get(self, request):
    #     form = HomeForm()
    #     return render(request,self.template_name,{'form': form})

    def get_batch_ids(self, request):
        batchids = Reddit.data_collection.database_interactions.get_all_batchIds_from_db()
        return render(request,self.template_name,{'batchids': batchids})
    
    def post(self, request):
        form = DataForm(request.POST)
        if form.is_valid():
            subreddit = form.cleaned_data['subreddit']
            sort_by = form.cleaned_data['sort_by']
            limit = form.cleaned_data['limit']
            Reddit.data_collection.collect_submission_ids(subreddit,sort_by,limit)

        args = {'form': form,'subreddit': subreddit}
        return render(request, self.template_name, args)




class TrackDataView(generic.ListView):
    template_name = 'karmachart/track_data.html'

    def get_queryset(self):
        """Return the last five published questions."""
        return 'testing'
    
    def get(self, request):
        form = DataForm()
        return render(request,self.template_name,{'form': form})

    def post(self, request):
        form = DataForm(request.POST)
        if form.is_valid():
            subreddit = form.cleaned_data['subreddit']
            sort_by = form.cleaned_data['sort_by']
            limit = form.cleaned_data['limit']
            Reddit.data_collection.collect_submission_ids(subreddit,sort_by,limit)

        args = {'form': form,'subreddit': subreddit}
        return render(request, self.template_name, args)











