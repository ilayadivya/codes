from django.urls import path
from . import views

urlpatterns = [
	path('hello', views.HelloView.as_view(), name ='hello'),
	path('bankDetails', views.HelloView.as_view(), name ='hello'),
	path('branches', views.Branch.as_view(), name ='branch'),
]
