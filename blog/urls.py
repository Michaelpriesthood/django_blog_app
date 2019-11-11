from django.urls import path
from . import views


urlpatterns = [
	path('', views.home, name='blog-home'),
	path('<int:pk>/', views.post_details, name='blog-details')
]