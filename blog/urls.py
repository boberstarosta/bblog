from django.urls import path

from blog import views


app_name = 'blog'

urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
	path('<int:pk>/', views.PostDetailView.as_view(), name='detail'),
	path('new-post/', views.CreatePostView.as_view(), name='create_post')
]
