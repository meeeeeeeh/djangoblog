from django.urls import path
from . import views


urlpatterns = [
    path('post/<int:comment_pk>/comment_edit/', views.comment_edit, name='comment_edit'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/list', views.post_list, name='post_list'),
    path('post/<int:post_pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:post_pk>/edit/', views.post_edit, name='post_edit'),
    path('delete/<int:post_pk>', views.delete_post, name='delete_post'),
    path('delete/comment/<int:comment_pk>', views.delete_comment, name='delete_comment'),
    path('post/<int:post_pk>/comment_new', views.comment_new, name='comment_new'),

]
