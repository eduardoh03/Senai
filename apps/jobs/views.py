import pprint

from django.shortcuts import render, redirect, get_object_or_404

from .forms import JobForm
from .models import Job


# Create your views here.
def jobs(request):
    jobs = Job.objects.all()

    dados = {
        "jobs": jobs
    }
    return render(request, "jobs.html", dados)


def job(request, id):
    job = Job.objects.get(id=id)
    dados = {
        "job": job
    }
    return render(request, "vaga.html", dados)


def creat_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            if request.user.is_authenticated:
                form.save(user=request.user)
                return redirect('pagina_jobs')
            else:
                form.add_error(None, 'User not authenticated')
    else:
        form = JobForm()
    return render(request, "criar_vaga.html", {'form': form})


def update_job(request, job_id):
    instance = get_object_or_404(Job, id=job_id)
    form = JobForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('pagina_jobs')
    else:
        print(form.errors)
    return render(request, "atualizar_vaga.html", {'form': form})


def delete_job(request, job_id):
    instance = get_object_or_404(Job, id=job_id)
    instance.delete()
    return redirect('pagina_jobs')
