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
    form = JobForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('pagina_jobs')
    else:
        print(form.errors)
    return render(request, "criar_vaga.html", {'form': form})

def update_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    form = JobForm(request.POST or None, request.FILES or None, instance=job)
    if form.is_valid():
        form.save()
        return redirect('pagina_jobs')
    else:
        print(form.errors)
    return render(request, "atualizar_vaga.html", {'form': form})
