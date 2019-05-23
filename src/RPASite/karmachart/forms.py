from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

class DataForm(forms.Form):
    subreddit = forms.CharField()
    sort_by = forms.CharField()
    limit = forms.IntegerField(max_value=50,min_value=1)

