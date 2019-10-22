from django.urls import path

from blog import views


app_name = 'blog'

urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
	path('post/<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='update'),
	path('post/create/', views.PostCreateView.as_view(), name='create_post')
]
