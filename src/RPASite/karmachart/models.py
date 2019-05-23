# Create your models here.
import datetime
from django.db import models
from django.utils import timezone



class Job(models.Model):
    job_type = models.CharField(max_length=200)
    limit = models.IntegerField()
    sort_by = models.CharField(max_length=200)
    subreddit = models.CharField(max_length=200)
    batch_id = models.CharField(max_length=200)
    submission_id = models.CharField(max_length=200)
    scheduled_time = models.CharField(max_length=200)
    status = models.IntegerField()
    # def was_published_recently(self):
    #     return self.pub_date >= timezone.now() - datetime.timedelta(days=1)    
    def __str__(self):
        return self.job_type    


class ProcessQueue(models.Model):
    jobid = models.TextField(db_column='jobId', unique=True)  # Field name made lowercase.
    jobtype = models.TextField(db_column='jobType')  # Field name made lowercase.
    limit = models.IntegerField(blank=True, null=True)
    sortby = models.TextField(db_column='sortBy', blank=True, null=True)  # Field name made lowercase.
    subreddit = models.TextField(blank=True, null=True)
    batchid = models.TextField(db_column='batchId', blank=True, null=True)  # Field name made lowercase.
    submissionid = models.TextField(db_column='submissionId', blank=True, null=True)  # Field name made lowercase.
    scheduledtime = models.TextField(db_column='scheduledTime')  # Field name made lowercase.
    status = models.IntegerField()



class SubmissionData(models.Model):
    submissionid = models.TextField(db_column='submissionId')  # Field name made lowercase.
    batchid = models.TextField(db_column='BatchId')  # Field name made lowercase.
    created = models.TextField()
    number_1_hour = models.TextField(db_column='1_hour', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2_hour = models.TextField(db_column='2_hour', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_5_hour = models.TextField(db_column='5_hour', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_8_hour = models.TextField(db_column='8_hour', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_12_hour = models.TextField(db_column='12_hour', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_24_hour = models.TextField(db_column='24_hour', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_48_hour = models.TextField(db_column='48_hour', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.





class Submissions(models.Model):
    submissionid = models.TextField(db_column='SubmissionID', primary_key=True)  # Field name made lowercase.
    submissionname = models.TextField(db_column='SubmissionName', blank=True, null=True)  # Field name made lowercase.
    batchid = models.TextField(db_column='BatchId', blank=True, null=True)  # Field name made lowercase.
    create_datetime = models.TextField(blank=True, null=True)


