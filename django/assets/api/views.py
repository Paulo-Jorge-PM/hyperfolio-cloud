from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer, PostsSerializer, TextSerializer, ArtifactSerializer, ActivitySerializer

from drf_spectacular.utils import extend_schema, OpenApiParameter

from posts.models import Post, Text, Artifact, Activity


# Auth service
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


# Posts service
class PostsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows posts to be viewed or edited.
    """


    queryset = Post.objects.all().order_by("-id")
    serializer_class = PostsSerializer
    permission_classes = [permissions.IsAuthenticated]


class TextViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows texts to be viewed or edited.
    """

    queryset = Text.objects.all().order_by("-id")
    serializer_class = TextSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    @extend_schema(
        # extra parameters added to the schema
        parameters=[OpenApiParameter(name='postId', description='Filter by postId', required=False, type=int),
        ])
    def list(self, request):
        # your non-standard behaviour
        return super().list(request)

class ArtifactViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows artifacts to be viewed or edited.
    """

    queryset = Artifact.objects.all().order_by("-id")
    serializer_class = ArtifactSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    @extend_schema(
        # extra parameters added to the schema
        parameters=[OpenApiParameter(name='postId', description='Filter by postId', required=False, type=str),
        ])
    def list(self, request):
        print("??????????????????????????????????????????????")
        print(request)
        # your non-standard behaviour
        return super().list(request)

class ActivityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows activities to be viewed or edited.
    """

    queryset = Activity.objects.all().order_by("-id")
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAuthenticated]
    
    @extend_schema(
        # extra parameters added to the schema
        parameters=[OpenApiParameter(name='postId', description='Filter by postId', required=False, type=int),
        ])
    def list(self, request):
        # your non-standard behaviour
        return super().list(request)

