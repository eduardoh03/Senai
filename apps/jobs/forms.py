from django import forms

from apps.jobs.models import Job


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ['user', ]

    def save(self, commit=False, user=None):
        job = super(JobForm, self).save(commit=False)
        job.user = user
        commit = True
        if commit:
            job.save()
        return job
