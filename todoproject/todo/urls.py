from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # Page d'accueil (liste des tâches)

    path('add/', views.add_task, name='add_task'),
    # Ajouter une nouvelle tâche
    
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'), 
    # Supprimer une tâche
]
