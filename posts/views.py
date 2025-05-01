from rest_framework.views import APIView
from rest_framework.response import Response

from posts.models import Post

class PostListView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        return Response({"posts": posts})