from django.contrib.auth.models import User, Group
from posts.models import Post, Text, Artifact, Activity, Asset
from rest_framework import serializers

# Auth service
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'url', 'name']


# Posts service
class PostsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'user', 'title', 'body', 'thumbnail', 'categories', 'typePost', 'typeId', 'rate', 'dateCreated', 'views', 'privacy', 'assets', 'comments', "jobs", "skills", "persons"]
        
# Assets service
class AssetsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Asset
        fields = ['id', 'user', 'fileUpload', 'fileLink', 'dateCreated', 'fileTye']
        
class TextSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Text
        fields = ['id', 'postId', 'withPersons']
        
class ArtifactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Artifact
        fields = ['id', 'postId', 'categories', 'organizations', 'withPersons']
        
class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Activity
        fields = ['id', 'postId', 'dateStart', 'dateEnd', 'categories', 'organizations', 'locations', 'withPersons']
