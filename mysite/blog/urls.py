from django.urls import path
from blog import views

urlpatterns=[
    path('',views.PostListView.as_view(),name='post_list'),
    path('post/<int:pk>/',views.PostDetailView.as_view(),name='post_detail'),
    path('post/new/',views.PostCreateView.as_view(),name='create'),
    path('post/<int:pk>/update/',views.PostUpdateView.as_view(),name='update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(),name='delete'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
    ]