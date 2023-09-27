from django import forms

from apps.jobs.models import Job


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = "__all__"
