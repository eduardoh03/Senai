from django import forms

from apps.jobs.models import Job


class JobUpdateForm(forms.ModelForm):
    salario = forms.DecimalField(max_digits=10, decimal_places=2, localize=True)

    class Meta:
        model = Job
        fields = '__all__'


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
