from django.urls import path
#from django.contrib.auth import views as auth_views

from . import views 

urlpatterns = [
	path('', views.logIn, name='login'),
	path('list/', views.list, name='list'),

]