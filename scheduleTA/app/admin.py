from django.contrib import admin

# Register your models here.
from app.models import User, Course, Class
admin.site.register(User)
admin.site.register(Course)
admin.site.register(Class)