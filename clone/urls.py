from django.urls import path 
from . import views

urlpatterns=[
   path('',views.home, name='home'),
   path('logout/', views.logoutUser, name='logout'),
   path('updateprofile/$',views.update_profile,name='editprofile'),
]