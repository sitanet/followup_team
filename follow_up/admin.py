
from django.contrib import admin

from follow_up.models import Comment, Member

# Register your models here.
admin.site.register(Member)
admin.site.register(Comment)