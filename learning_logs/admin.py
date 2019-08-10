from django.contrib import admin

# Register your models here.
#注册Topic
from django.contrib import admin
from learning_logs.models import Topic,Entry
admin.site.register(Topic)
admin.site.register(Entry)