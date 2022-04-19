from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('delete_data/<int:id>', views.deleteData, name="delete_data"),
    path('update_data/<int:id>', views.updateData, name="update_data")
]
