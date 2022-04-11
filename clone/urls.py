from django.urls import path 
from . import views
from .views import ProfileList,ProjectList

urlpatterns=[
   path('',views.home, name='home'),
   path('logout/', views.logoutUser, name='logout'),
   path('profile/',views.profile,name = 'profile'),
   # path('updateprofile/',views.update_profile,name='updateprofile'),
   path('newproject/',views.new_project,name='newproject'),
   path('comment/<int:id>/',views.comment,name='comment'),
   path('project/<int:id>/',views.project,name='project'),
   path('projects/', ProjectList.as_view()),
   path('profiles/', ProfileList.as_view()),
   path('ratings/<int:id>/',views.rate,name='ratings'),

]