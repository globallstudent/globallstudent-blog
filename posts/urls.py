from django.urls import path
from posts.apis import PostCreateAPIView, PostListAPIView, PostDetailAPIView
from posts import views

urlpatterns = [
    path('all/', PostListAPIView.as_view()),
    path('<int:pk>/', PostDetailAPIView.as_view()),
    path('create/', PostCreateAPIView.as_view()),

    path('hello/', views.hello_world, name="hello_world")
]
