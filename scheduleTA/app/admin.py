from django.contrib import admin

# Register your models here.
from app.models import User, Course, Section
admin.site.register(User)
admin.site.register(Course)
admin.site.register(Section)