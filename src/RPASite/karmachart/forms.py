from django import forms
from .models import Job, Submissions, SortMethod
class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

class DataForm(forms.Form):
    subreddit = forms.CharField()
    sort_by = forms.ModelChoiceField(queryset = SortMethod.objects.all(), initial=0)
    limit = forms.IntegerField(max_value=50,min_value=1)

class SelectBatch(forms.Form):
    batch = forms.ChoiceField(widget=forms.Select(attrs={'batch': 'form-control'}))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['batch'].choices= [(batch.batchid) for batch in Submissions.objects.all()]

