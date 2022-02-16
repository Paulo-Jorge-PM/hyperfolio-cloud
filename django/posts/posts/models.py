from django.db import models
#from django.contrib.auth.models import User

from datetime import date, datetime

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    timestamp = datetime.now().timestamp()
    return 'static/assets/user_{0}/{1}'.format(instance.user, str(timestamp)+"_"+filename)

#def json_default():
#    return {"var":"x"}

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

    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.IntegerField(blank=False)
    
    title = models.CharField(max_length=255, blank=False)
    body = models.TextField(max_length=10000, blank=True)
    #thumbnail = models.CharField(max_length=255, blank=True, default="01-image.jpg")
    thumbnail = models.JSONField(default=list, null=True, blank=True)
    typePost = models.CharField(
                                choices=TYPES_CHOICE,
                                default='Artifact',
                                max_length=20, 
                                blank=False
                                )
    typeId = models.IntegerField(blank=False, default=0)
    rate = models.CharField(max_length=255, blank=True)
    dateCreated = models.DateField(blank=False, default=date.today, editable=False)
    
    views = models.IntegerField(blank=False, default=0)
    privacy = models.CharField(
                                choices=PRIVACY_CHOICE,
                                default='Public',
                                max_length=20, 
                                blank=False
                                )
    categories = models.JSONField(default=list, null=True, blank=True)
                      
    assets = models.JSONField(default=list, null=True, blank=True)
    comments = models.JSONField(default=list, null=True, blank=True)
    
    #jobs = models.TextField(max_length=6000, null=True, blank=True)
    #jobs = models.TextField(max_length=6000, null=True, blank=True, default=list) #defualt=list / default=dict 
    jobs = models.JSONField(default=list, null=True, blank=True)
    skills = models.JSONField(default=list, null=True, blank=True)
    persons = models.JSONField(default=list, null=True, blank=True)

    
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
        return "ID: " + str(self.id) + " | User: " + str(self.user) + " | Title: " + self.title


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
        
        
class Asset(models.Model):
    FILES_CHOICES = [
        ('Misc', 'Misc'),
        ('Image', 'Image'),
        ('Animation', 'Animation'),
        ('Video', 'Video'),
        ('Sound', 'Sound'),
        ('Document', 'Document'),
        ('3DModel', '3DModel'),
    ]

    user = models.IntegerField(blank=False)
    fileLink = models.CharField(max_length=255, blank=True)
    fileUpload = models.FileField(upload_to=user_directory_path, blank=True)
    dateCreated = models.DateField(blank=True, default=date.today, editable=False)
    fileTye = models.CharField(
                                choices=FILES_CHOICES,
                                default='Misc',
                                max_length=20, 
                                blank=True
                                )

    def __str__(self):
        return "UserId: " + str(self.user) + " | ID: " + str(self.id)
