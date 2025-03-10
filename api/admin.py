from django.contrib import admin
from .models import User,JobPostion,JobApplication
# Register your models here.
admin.site.register(JobApplication)
admin.site.register(User)
admin.site.register(JobPostion)