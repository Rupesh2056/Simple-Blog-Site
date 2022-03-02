from django.urls import path,include
from . import views 

urlpatterns = [
    path('', views.PostListView.as_view(),name="blog-index"),
    path('about/', views.About,name="blog-about"),
    path('post/<int:pk>/', views.PostDetailView.as_view(),name="post-detail"),
    path('newpost/', views.PostCreateView.as_view(),name="post-create"),
    path('post/<int:pk>/edit/', views.PostEditView.as_view(),name="post-edit"),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(),name="post-delete"),
]
