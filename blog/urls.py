from django.urls import path
from .views import HomeBlogListView, HomeBlogDetailView, HomeBlogCreateView, HomeBlogDeleteView, HomeBlogUpdateView

urlpatterns = [
    path('post/new/', HomeBlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/', HomeBlogDetailView.as_view(), name='post_detail'),
    path('post/update/<int:pk>/', HomeBlogUpdateView.as_view(), name='post_update'),
    path('post/delete/<int:pk>/', HomeBlogDeleteView.as_view(), name='post_delete'),
    path('', HomeBlogListView.as_view(), name='home'),
]