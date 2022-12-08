from django.shortcuts import render, redirect
from django.views import View
from classes import UserClass
from .models import User, Course, Section


# Helper methods
# Session
def isLoggedIn(session):
    if 'name' in session:
        return len(session['name']) > 0
    return False


def isAdminLoggedIn(session):
    if isLoggedIn(session):
        # check if the logged-in user has admin role
        if UserClass.UserClass.getRole(None, session['name']) == 'A':
            return True
    return False


# Create your views here.
class Home(View):
    def get(self, request):
        return render(request, 'home.html', {})

    def post(self, request):
        form_submitted_name = request.POST.get('name')
        form_submitted_password = request.POST.get('password')

        if not UserClass.UserClass.authenticate(self, form_submitted_name, form_submitted_password):
            return render(request, 'home.html', {"message": "Login Error: invalid input, try again."})

        request.session["name"] = form_submitted_name.upper()
        return redirect("homepage_0")


class Homepage_0(View):
    def get(self, request):
        # handle unauthorized access by redirecting them to the login page
        if isLoggedIn(request.session):
            name = request.session["name"]
            role = UserClass.UserClass.getRole(self, name)
            return render(request, "homepage_0.html", {"name": name, "role": role})
        return redirect("home")


class CreateUser(View):
    def get(self, request):
        # handle unauthorized access by showing them 403 error
        if isAdminLoggedIn(request.session):
            return render(request, "create_user.html", {})
        return render(request, '403.html', {})

    def post(self, request):
        # handle unauthorized access by showing them 403 error
        if isAdminLoggedIn(request.session):
            input_name = request.POST.get('input_name')
            input_pw1 = request.POST.get('input_pw1')
            input_pw2 = request.POST.get('input_pw2')
            input_role = request.POST.get('input_role')
            if input_pw1 != input_pw2:
                return render(request, 'create_user.html', {"message": "ERROR: Passwords do NOT match, try again."})
            else:
                new_user = User(name=input_name, password=input_pw1, role=input_role)
                if UserClass.UserClass.addUser(self, new_user):
                    return render(request, 'create_user.html', {"message": "SUCCESS! User added successfully."})
                else:
                    return render(request, 'create_user.html', {"message": "ERROR: Username already exists in database, try again."})
        return render(request, '403.html', {})


class ViewUser(View):
    def get(self, request):
        # handle unauthorized access by showing them 403 error
        if isAdminLoggedIn(request.session):
            return render(request, 'view_user.html', {"users": UserClass.UserClass.getAllUsers(self)})
        return render(request, '403.html', {})