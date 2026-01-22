from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.postListView, name="postListView"),
    path('category/<str:categoryName>/', views.postListView, name="postListCategory"),
    path('post/<int:postID>', views.postDetailView, name="postDetailView"),
    path('author/<authorName>', views.postListView, name="postAuthorList")
]
