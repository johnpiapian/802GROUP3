from django.shortcuts import render, redirect
from django.views import View


# Create your views here.
class Home(View):
    def get(self, request):
        return render(request, 'home.html', {})
    def post(self, request):
        return redirect('/edit_profile')
class EditProfile(View):
    def get(self, request):
        return render(request, 'edit.html', {})
class CreateNewUser(View):
    def get(self, request):
        return render(request, 'new_user.html', {})
class CreateNewCourse(View):
    def get(self, request):
        return render(request, 'new_course.html', {})