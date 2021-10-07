from django.urls import path
from . import views


app_name= "articles"

urlpatterns = [
    path('', views.index, name= 'index'),
    path('create', views.create, name= 'create'),
    path('search', views.search, name= 'search'),
    path('<int:id>/show', views.show, name= 'show'),
    path('<int:id>/edit', views.edit, name= 'edit'),
    path('<int:id>/delete', views.delete, name= 'delete'),
]
