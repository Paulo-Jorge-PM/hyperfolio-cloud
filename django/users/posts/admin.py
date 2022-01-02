from django.contrib import admin

from .models import Post, Text, Artifact, Activity

admin.site.register(Post)
admin.site.register(Text)
admin.site.register(Artifact)
admin.site.register(Activity)
