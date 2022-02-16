from rest_framework import viewsets

from posts.models import Post
from posts.serializers import PostsSerializer

class PostsViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Post.objects.all()
    serializer_class = PostsSerializer
    print("#############################")
    def get_queryset(self):
        """ allow rest api to filter by submissions """
        queryset = Post.objects.all()
        user = self.request.query_params.get('user', None)
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print(user)
        if user is not None:
            queryset = queryset.filter(user=user)
        
        return queryset
        
