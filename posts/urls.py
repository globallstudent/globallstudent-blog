from django.urls import path
from posts.views import PostListView

urlpatterns = [
    path('all', PostListView.as_view())
]