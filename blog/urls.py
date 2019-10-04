from django.urls import path
from . import views
from .views import PostList, PostDetail

urlpatterns = [
    path('',PostList.as_view(), name='post_list'),
    path('delete/<int:pk>/', views.post_delete, name='post_delete'),
    path('post/<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit', views.post_edit, name='post_edit'),
    path('post/dropdown/', views.post_dropdown, name='post_dropdown'),
    path('post/search/', views.post_search, name='post_search'),
	
]
