from django.urls import path, include
from . import views

app_name = 'api-v1'

urlpatterns = [
    path('post/', views.PostList ,name='api-post-list'),
    path('post/<int:pk>/', views.PostDetail ,name='api-post-detail'),

]
