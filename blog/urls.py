from django.urls import path
from . import views
# from django.contrib.auth import LoginView


urlpatterns = [
	path('', views.home, name='blog-home'),
	path('<int:post_id>/', views.post_details, name='blog-details'),

]