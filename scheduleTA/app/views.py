from django.shortcuts import render, redirect
from django.views import View
from classes import UserClass
from .models import User, Course, Section

# Create your views here.
class Home(View):
    def get(self, request):
        return render(request, 'home.html', {})
    def post(self, request):
        form_submitted_name = request.POST.get('name')
        form_submitted_password = request.POST.get('password')
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


class CreateUser(View):
    def get(self, request):
        ## retrieve the logged in user's role from session
        logged_in_user = request.session["name"]
        # role = User.objects.filter(name=logged_in_user).values_list('role',flat=True)[0]

        if UserClass.UserClass.getRole(self, logged_in_user) == 'A': # only an Admin with role 'A' can access the add users page
            return render(request, "create_user.html", {})
        else: # else = User's role is NOT Administrator, not authorized
            return render(request, '403.html', {})

    def post(self, request):
        input_name = request.POST.get('input_name')
        input_pw1 = request.POST.get('input_pw1')
        input_pw2 = request.POST.get('input_pw2')
        input_role = request.POST.get('input_role')

        if input_pw1 != input_pw2:
            return render(request, 'create_user.html',
                          {"message": "ERROR: Passwords do NOT match, try again."})
        else:
            new_user = User(name=input_name, password=input_pw1, role=input_role)
            if UserClass.UserClass.addUser(self, new_user):
                return render(request, 'create_user.html', {"message": "SUCCESS! User added successfully."})
            else:
                return render(request, 'create_user.html', {"message": "ERROR: Username already exists in database, try again."})

