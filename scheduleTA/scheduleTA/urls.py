"""scheduleTA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import Home, Homepage_0, CreateUser, ViewUser, ViewUserSingle, Logout, UpdateUser, DeleteUser, Profile, \
    ManageCourse, DeleteCourse, CreateCourse

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name='home'), ## look @ "views.py -> class Home" to see what this loads
    path('homepage_0/', Homepage_0.as_view(), name='homepage_0'),

    # User stuff
    path('create_user/', CreateUser.as_view(), name='create_user'),
    path('update_user/', UpdateUser.as_view(), name='update_user'),
    path('delete_user/', DeleteUser.as_view(), name='delete_user'),
    path('view_user/', ViewUser.as_view(), name='view_user'),
    path('view_user/<name>', ViewUserSingle.as_view(), name='view_user_single'),
    path('profile/', Profile.as_view(), name='profile'),
    path('logout/', Logout.as_view(), name='logout'),

    # Course
    path('manage_course/', ManageCourse.as_view(), name='manage_course'),
    path('create_course/', CreateCourse.as_view(), name='create_course'),
    path('manage_course/delete/<int:courseID>', DeleteCourse.as_view(), name='delete_course')
]
