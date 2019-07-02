from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, HttpResponse
from django.urls import reverse
import requests
from django.views import generic
from .models import Job, Submissions
from .forms import NameForm, DataForm
from Reddit import data_collection, submission_data, data_visualization
from background_task import background
import datetime, time
from django.views.generic import TemplateView
from pygal.style import DarkStyle, DarkSolarizedStyle

from .charts import submissionPieChart, batchPieChart


class IndexView(TemplateView):
    template_name = 'karmachart/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        # Instantiate our chart. We'll keep the size/style/etc.
        # config here in the view instead of `charts.py`.
        cht_fruits = submissionPieChart(
            height=600,
            width=800,
            explicit_size=True,
            style=DarkStyle,
            fill = True
        )

        # Call the `.generate()` method on our chart object
        # and pass it to template context.
        context['cht_fruits'] = cht_fruits.generate()
        return context


class TrackDataView(generic.ListView):
    template_name = 'karmachart/track_data.html'
    
    def get(self, request):
        form = DataForm()
        return render(request,self.template_name,{'form': form})

    def post(self, request):
        form = DataForm(request.POST)
        if form.is_valid():
            subreddit = form.cleaned_data['subreddit']
            sort_by = form.cleaned_data['sort_by']
            limit = form.cleaned_data['limit']
            data_collection.collect_submission_ids(subreddit,sort_by,limit)

        args = {'form': form,'subreddit': subreddit}
        return render(request, self.template_name, args)

    def schedule(self,request):
        return "test"

class SubmissionsView(generic.ListView):
    template_name = 'karmachart/submissions.html'    
    
    def get(self, request):
        submissions = Submissions.objects.all()
        subids = []

        for item in submissions:
            subids.append(item.submissionid)
        score_list = submission_data.get_multi_score(subids)
        idx = 0
        
        for item in submissions:
            item.score = score_list[idx]
            idx += 1

        args = {'submissions': submissions}
        return render(request,self.template_name,args)
        
    

class SpecificBatchView(generic.ListView):
    template_name = 'karmachart/batch.html'      
    def get(self, request):
        currentbatchid = request.GET.get('batchid')
        if not currentbatchid:
            submissions = Submissions.objects.filter(batchid = "59ac5921-6493-423e-a80d-edd255aaf498")
            currentbatchid = "59ac5921-6493-423e-a80d-edd255aaf498"
        else:
            submissions = Submissions.objects.filter(batchid = currentbatchid )

        subids = []
        for item in submissions:
            subids.append(item.submissionid)
        score_list = submission_data.get_multi_score(subids)
        idx = 0
        
        for item in submissions:
            item.score = score_list[idx]
            idx += 1
        first = submissions[1]
        cht_fruits = batchPieChart(
            currentbatchid,
            height=600,
            width=1200,
            explicit_size=True,
            style=DarkSolarizedStyle
             
        )
        batches = Submissions.objects.values('batchid').distinct()
        
        args = {'submissions': submissions, 'first': first, 'cht_fruits': cht_fruits.generate(),'batches':batches}
        return render(request,self.template_name,args)


    def post(self, request):
        currentbatchid = request.POST.get('batchid')
        if not currentbatchid:
            submissions = Submissions.objects.filter(batchid = "59ac5921-6493-423e-a80d-edd255aaf498")
            currentbatchid = "59ac5921-6493-423e-a80d-edd255aaf498"
        else:
            submissions = Submissions.objects.filter(batchid = currentbatchid )

        subids = []
        for item in submissions:
            subids.append(item.submissionid)
        score_list = submission_data.get_multi_score(subids)
        idx = 0
        
        for item in submissions:
            item.score = score_list[idx]
            idx += 1
        first = submissions[1]
        cht_fruits = batchPieChart(
            currentbatchid,
            height=600,
            width=1200,
            explicit_size=True,
            style=DarkSolarizedStyle
             
        )
        batches = Submissions.objects.values('batchid').distinct()
        
        args = {'submissions': submissions, 'first': first, 'cht_fruits': cht_fruits.generate(),'batches':batches}
        return render(request,self.template_name,args)        


        
    








