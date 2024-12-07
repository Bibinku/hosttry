from django.urls import path
from Backend import views

urlpatterns=[

   path('indexpage/',views.indexpage,name='indexpage'),
   path('detailspage/',views.detailspage,name='detailspage'),

 ]


