from django.urls import path
from .views import job, jobs, create_job, update_job, delete_job

urlpatterns = [

    path('', jobs, name="pagina_jobs"),
    path('/<int:id>/', job, name="ver_job"),
    path('update/<int:job_id>/', update_job, name="update_job"),
    path('create_job/', create_job, name="pagina_jobs_create_job"),
    path('delete_job/<int:job_id>/', delete_job, name="delete_job"),

]
