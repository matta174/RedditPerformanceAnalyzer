# Create your models here.
import datetime
from django.db import models
from django.utils import timezone



class Job(models.Model):
    job_type = models.CharField(max_length=200)
    limit = models.IntegerField(max_length=200)
    sort_by = models.CharField(max_length=200)
    subreddit = models.CharField(max_length=200)
    batch_id = models.CharField(max_length=200)
    submission_id = models.CharField(max_length=200)
    scheduled_time = models.CharField(max_length=200)
    status = models.IntegerField(max_length=200)
    # def was_published_recently(self):
    #     return self.pub_date >= timezone.now() - datetime.timedelta(days=1)    
    def __str__(self):
        return self.job_type    