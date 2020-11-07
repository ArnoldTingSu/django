from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('new', views.new),
    path('create', views.create),
    path('<int:id>', views.show),
    path('edit/<int:id>', views.edit),
    path('delete/<int:id>', views.delete)
]