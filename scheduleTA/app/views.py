from django.shortcuts import render, redirect
from django.views import View
from classes import UserClass
from .models import User, Course, Section

# Create your views here.
class Home(View):
    def get(self, request):
        return render(request, 'home.html', {})
    def post(self, request):
        form_submitted_name = request.POST['name']
        form_submitted_password = request.POST['password']
        if not UserClass.UserClass.userExists(self,form_submitted_name):
            return render(request, 'home.html', {"message": "Login Error: Invalid username, try again."})
        if not UserClass.UserClass.passwordCorrect(self, UserClass.UserClass.getUser(self, form_submitted_name), form_submitted_password):
            return render(request, 'home.html', {"message": "Login Error: Invalid password, try again."})
        request.session["name"] = form_submitted_name
        return redirect("homepage_0")

class Homepage_0(View):
    def get(self, request):
        m = request.session["name"]
        role = User.objects.filter(name=m).values_list('role',flat=True)
        return render(request, "homepage_0.html", {"name":m,"role":role})