from django.urls import path
from Backend import views

urlpatterns = [

    path('indexpage/', views.indexpage, name='indexpage'),
    path('detailspage/', views.detailspage, name='detailspage'),
    path('savedetails/', views.savedetails, name='savedetails'),
    path('displaydetails/', views.displaydetails, name='displaydetails'),
    path('editdetails/<int:Did>/', views.editdetails, name="editdetails"),
    path('updatedetails/<int:Uid>/', views.updatedetails, name="updatedetails"),
    path('deletedetails/<int:Delid>/', views.deletedetails, name="deletedetails"),
    path('adminlogin/', views.adminlogin, name="adminlogin"),
    path('admin/', views.admin, name="admin"),

]
