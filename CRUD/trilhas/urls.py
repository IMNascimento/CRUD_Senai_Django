from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('adicionar', views.create, name="create"),
    path('editar/<int:id>', views.edit, name="edit"),
    path('atualizar/<int:id>', views.update, name="update"),
    path('deletar/<int:id>', views.delete, name="delete"),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
]
