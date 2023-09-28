from django.urls import path
from .views import blog, details_blog

urlpatterns = [
    path('blog/', blog, name="pagina_blog"),
    path('blog/<int:blog_id>', details_blog, name="blog_detalhes"),

]
