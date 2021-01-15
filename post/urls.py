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
    path('post/<int:post_pk>/post_like_or_dislike/', views.post_like_or_dislike, name='post_like_or_dislike'),
    path('post/draft/list/', views.draft_list, name='draft_list'),
    path('post/publish/<int:post_pk>/', views.publish, name='publish'),
    path('post/tag_list/<int:tag_pk>/', views.tag_list, name='tag_list'),
    path('post/category_posts/<int:category_pk>/', views.category_posts, name='category_posts'),
    path('post/recommendations/', views.recommendations, name='recommendations'),
    path('post/add_to_favorite/<int:post_pk>/', views.add_to_favorite, name='add_to_favorite'),
    path('post/favorites/', views.favorites, name='favorites'),

]
