from django.urls import path
from . import views
from .views import (
	PostListView,
	PostCreateView,
	PostUpdateView,
	PostDeleteView,
	UserPostListView
)


urlpatterns = [
	path('', PostListView.as_view(), name='blog-home'),
	path('user/<str:username>/', UserPostListView.as_view(), name='user-post'),
	path('post/<int:post_id>/', views.post_detail, name='post-detail'),
	path('post/new/', PostCreateView.as_view(), name='post-create'),
	path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
	path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

] 