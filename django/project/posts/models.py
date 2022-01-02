from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    TYPES_CHOICE = [
        ('Text', 'Text'),
        ('Activity', 'Activity'),
        ('Artifact', 'Artifact'),
    ]
    
    PRIVACY_CHOICE = [
        ('Public', 'Public'),
        ('Friends', 'Friends'),
        ('Me', 'Me'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    title = models.CharField(max_length=255, blank=False)
    body = models.TextField(max_length=10000, blank=True)
    thumbnail = models.CharField(max_length=255, blank=True)
    tags = models.TextField(max_length=1000, blank=True)
    typePost = models.CharField(
                                choices=TYPES_CHOICE,
                                default='Text',
                                max_length=20, 
                                blank=False
                                )
    typeId = models.IntegerField(blank=False)
    rate = models.CharField(max_length=255, blank=True)
    dateCreated = models.DateField(null=True, blank=False)
    
    views = models.IntegerField(blank=False, default=0)
    privacy = models.CharField(
                                choices=PRIVACY_CHOICE,
                                default='Public',
                                max_length=20, 
                                blank=False
                                )
    assets = models.TextField(max_length=3000, null=True, blank=True)
    comments = models.TextField(max_length=6000, null=True, blank=True)
    
    """assets = models.ManyToManyField(
        Assets,
        verbose_name=_('assets'),
        blank=True,
        help_text=_(
            'The assets this post belongs to.'
        ),
        #related_name="post_set",
        #related_query_name="post",
    )"""
    
    def __str__(self):
        return self.title


class Text(models.Model):

    postId = models.OneToOneField(Post, on_delete=models.CASCADE, to_field='id')
    withPersons = models.TextField(max_length=500, blank=True)
    
    def __str__(self):
        return str(self.postId)

class Artifact(models.Model):

    postId = models.OneToOneField(Post, on_delete=models.CASCADE, to_field='id')
    
    categories = models.TextField(max_length=1000, blank=True)
    organizations = models.TextField(max_length=1000, blank=True)
    withPersons = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return str(self.postId)


class Activity(models.Model):

    postId = models.OneToOneField(Post, on_delete=models.CASCADE, to_field='id')
    
    dateStart = models.DateField(null=True, blank=False)
    dateEnd = models.DateField(null=True, blank=True)
    
    categories = models.TextField(max_length=1000, blank=True)
    organizations = models.TextField(max_length=500, blank=True)
    locations = models.TextField(max_length=500, blank=True)
    withPersons = models.TextField(max_length=500, blank=True)
    
    def __str__(self):
        return str(self.postId)
