from rest_framework.decorators import *
from rest_framework.permissions import *
from rest_framework.response import *
from rest_framework import viewsets
from rest_framework.views import *
from rest_framework.generics import *
from Todo.models import *
from .serializers import *
from django.shortcuts import get_object_or_404, redirect
from .permissions import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .paginations import *

# Example of function based view for api
"""An function based api view that allows the user to get a list of all objects of post model and also creating a new one"""
"""@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def postList(request):
    if request.method == "GET":
        posts = Post.objects.filter(status=True)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)"""
"""An function based api view that allows the user to get a certain object of post model and deleting it or editing it"""
"""@api_view(["GET", "PUT", "DELETE"])
def postDetail(request, id):
    post = get_object_or_404(Post, pk=id, status=True)
    if request.method == "GET":
        serializer = PostSerializer(post)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = PostSerializer(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == "DELETE":
        post.delete()
        return Response({"detail": "Item removed successfully"}, status=status.HTTP_204_NO_CONTENT)
"""

# Example of class based view for api
"""An class based view api that inherits from APIView and allows the user to get a certain object of post model and deleting it or editing it"""
'''class PostDetail(APIView):
    """ getting detail of a post and edit + delete """
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def get(self, request, id):
        """retrieving the post data"""
        post = get_object_or_404(Post, pk=id, status=True)
        serializer = self.serializer_class(post)
        return Response(serializer.data)

    def put(self, request, id):
        """editing the post data"""
        post = get_object_or_404(Post, pk=id, status=True)
        serializer = PostSerializer(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

    def delete(self, request, id):
        """deleting a post"""
        post = get_object_or_404(Post, pk=id, status=True)
        post.delete()
        return Response({"detail": "Item removed successfully"}, status=status.HTTP_204_NO_CONTENT)
'''
"""An class based view api that inherits from APIView and allows the user to get a list of all objects of post model and also creating a new one"""
'''class PostList(APIView):
    """getting a list of posts and creating new post"""
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    def get(self, request):
        """retrieving a list of posts """
        posts = Post.objects.filter(status=True)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        """creating a post with provided data"""
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
'''

# Example of generic api views
"""An class based api view that inherits from ListCreateAPIView and allows the user to get a list of all objects of post model and also creating a new one"""
'''class PostList(ListCreateAPIView):
    """getting a list of posts and creating new post"""
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)'''
"""An class based api view that inherits from RetrieveUpdateDestroyAPIView and allows the user to get a certain object of post model and deleting it or editing it"""
'''class PostDetail(RetrieveUpdateDestroyAPIView):
    """getting a special post by its id and editing it or deleting it"""
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)'''


# Example of ModelViewSet api views
class TaskModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = {"author": ["exact"], "title": ["exact"], "status": ["exact"]}
    search_fields = ["title", "content"]
    ordering_fields = [
        "created_date",
    ]

    # pagination_class = pagination
    def get_queryset(self):
        user = self.request.user.id
        profile = get_object_or_404(Profile, user=user)
        queryset = Task.objects.filter(author=profile)
        return queryset
