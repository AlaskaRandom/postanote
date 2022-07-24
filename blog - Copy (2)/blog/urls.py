# blog/urls.py
from django.urls import path
from .views import HomePageView
from .views import HomePageView, BlogDetailView, BlogListView, BlogCreateView,BlogUpdateView, BlogDeleteView, COVID


urlpatterns = [
    path('post/delete/<int:pk>', BlogDeleteView.as_view(), name='post_delete'),
    path('post/edit/<int:pk>', BlogUpdateView.as_view(), name='post_edit'),
    path('post/new/',BlogCreateView.as_view(), name='post_new'),# new
    path('post/<int:pk>/', BlogDetailView.as_view(),name='post_detail'),
    path('',BlogListView.as_view(),name = 'home'),
    path('',HomePageView.as_view(),name = 'home'),
    path('covid',COVID.as_view(), name = 'covid')
]