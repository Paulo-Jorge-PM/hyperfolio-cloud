from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer, PostsSerializer, TextSerializer, ArtifactSerializer, ActivitySerializer, AssetsSerializer

from rest_framework.pagination import PageNumberPagination

from drf_spectacular.utils import extend_schema, OpenApiParameter

from posts.models import Post, Text, Artifact, Activity, Asset

from drf_spectacular.utils import extend_schema, OpenApiParameter

#from django.http import JsonResponse
#from django.core import serializers 

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


## CHANGE DEFAULT PAGE SIZE
class LargerPagination(PageNumberPagination):
    page_size = 200
    page_size_query_param = 'psize'
    max_page_size = 1000

# Posts service
class PostsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows posts to be viewed or edited.
    """

    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all().order_by("-id")
    serializer_class = PostsSerializer
    
    
    
    # Filter by params
    def get_queryset(self):
        """ allow rest api to filter by parameters """
        user = self.request.query_params.get('user', None)
        
        if user is not None:
            self.pagination_class = LargerPagination
            queryset = Post.objects.all().order_by("-id")
            queryset = queryset.filter(user=user)
            
            return queryset
            
        else:
            queryset = Post.objects.all().order_by("-id")
            
            return queryset
    
    # Add the new param field to swagger UI
    @extend_schema(
        methods=['GET'],
        # extra parameters added to the schema
        parameters=[OpenApiParameter(name='user', description='Filter by user id.', required=False, type=int),
                    OpenApiParameter(name='psize', description='Set results per page - Only for user parameter.', required=False, type=int),
        ])
    def list(self, request):
        # non-standard behaviour if needed, e.g.:
        # queryset = Post.objects.filter(user__exact=2).order_by("-id")
        # json_res = serializers.serialize('json',data)  
        # return JsonResponse(list(data.values()), safe=False)
        return super().list(request)
    
    

# Assets service
class AssetsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows assets to be viewed or edited.
    """


    queryset = Asset.objects.all().order_by("-id")
    serializer_class = AssetsSerializer
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

