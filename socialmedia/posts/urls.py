from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('new/', views.CreatePost.as_view(), name='create'),
    path('edit/<int:pk>/', views.PostUpdate.as_view(), name='edit'),
    path('<int:pk>/', views.PostDetail.as_view(), name='single'),
    path('delete/<int:pk>/', views.DeletePost.as_view(), name='delete'),
]
