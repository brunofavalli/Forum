from django.contrib import admin

# Register your models here.
from django.contrib import admin

from forum.models import Forum, Thread, Post, UserProfile

admin.site.register(Forum)
admin.site.register(Thread)
admin.site.register(Post)
admin.site.register(UserProfile)