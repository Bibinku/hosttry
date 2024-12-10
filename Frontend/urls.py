from django.urls import path
from Frontend import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('roomspage/<int:Aid>/', views.roomspage, name="roomspage"),
    path('contactpage/', views.contactpage, name="contactpage"),
    path('savecontact/', views.savecontact, name="savecontact"),
]
