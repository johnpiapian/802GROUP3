from django.shortcuts import render, redirect
from django.views import View
from classes import UserClass, CourseClass
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
        if isLoggedIn(request.session):
            return redirect("homepage_0")
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
        elif isLoggedIn(request.session):
            return render(request, '403.html', {})
        return redirect("home")

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
                    return render(request, 'create_user.html',
                                  {"message": "ERROR: Username already exists in database, try again."})
        return render(request, '403.html', {})


class ViewUser(View):
    def get(self, request):
        # handle unauthorized access by showing them 403 error
        if isAdminLoggedIn(request.session):
            return render(request, 'view_user.html', {"users": UserClass.UserClass.getAllUsers(self)})
        return render(request, '403.html', {})


class ViewUserSingle(View):
    def get(self, request, name):
        # handle unauthorized access by showing them 403 error
        if isAdminLoggedIn(request.session):
            return render(request, 'view_user_single.html',
                          {"type": "admin", "user": UserClass.UserClass.getUser(self, name)})
        return render(request, '403.html', {})


class UpdateUser(View):
    def post(self, request):
        # handle unauthorized access by showing them 403 error
        if isLoggedIn(request.session):
            input_id = request.POST.get('input_id')
            input_name = request.POST.get('input_name')
            input_pw1 = request.POST.get('input_pw1')
            input_pw2 = request.POST.get('input_pw2')
            input_role = request.POST.get('input_role')
            roles = ['A', 'P', 'T']

            # Need it for certain session management
            oldName = UserClass.UserClass.getUserByID(self, int(input_id)).name

            # non admin should be able to update only their profile
            if oldName != request.session['name'] and not isAdminLoggedIn(request.session):
                return render(request, '403.html', {})

            if len(input_pw1) > 0 and input_pw1 != input_pw2:
                return render(request, "base-error.html",
                              {"message": "ERROR: Passwords do NOT match, try again.", "url": "view_user"})
            elif input_role is not None and input_role not in roles:
                return render(request, "base-error.html",
                              {"message": "ERROR: invalid input role type, try again.", "url": "view_user"})
            else:
                userToUpdate = User(id=int(input_id), name=input_name, password=input_pw1, role=input_role)
                if UserClass.UserClass.updateUser(self, userToUpdate):
                    # update session name if we are updating self
                    if request.session['name'] == oldName:
                        request.session['name'] = input_name

                    if isAdminLoggedIn(request.session):
                        return redirect("view_user")
                    else:
                        return redirect("homepage_0")

        return render(request, '403.html', {})


class DeleteUser(View):
    def post(self, request):
        # handle unauthorized access
        if isLoggedIn(request.session):
            input_id = request.POST.get('input_id')
            input_name = request.POST.get('input_name')

            # non-admin user should only be able to delete their profile
            if input_name != request.session['name'] and not isAdminLoggedIn(request.session):
                return render(request, '403.html', {})

            if UserClass.UserClass.getUser(self, input_name).id == int(input_id) and UserClass.UserClass.deleteUser(self, input_name):
                if request.session['name'] == input_name:
                    return redirect("logout")
                return redirect("view_user")
        return render(request, '403.html', {})


class Profile(View):
    # handle unauthorized access by showing them 403 error
    def get(self, request):
        # handle unauthorized access by showing them 403 error
        if isAdminLoggedIn(request.session):
            return render(request, 'view_user_single.html',
                          {"type": "admin", "user": UserClass.UserClass.getUser(self, request.session['name'])})
        elif isLoggedIn(request.session):
            return render(request, 'view_user_single.html',
                          {"type": "user", "user": UserClass.UserClass.getUser(self, request.session['name'])})
        return render(request, '403.html', {})


class Logout(View):
    def get(self, request):
        if isLoggedIn(request.session):
            del request.session["name"]
            return redirect("home")
        return render(request, 'base-error.html', {"title": "Unexpected error!"})


# Course
class ManageCourse(View):
    def get(self, request):
        if isLoggedIn(request.session):
            return render(request, 'manage_course.html', {"courses": CourseClass.CourseClass.getAllCourses(self)})
        return render(request, '403.html', {})


class DeleteCourse(View):
    def get(self, request, courseID):
        if isLoggedIn(request.session):
            if CourseClass.CourseClass.deleteCourse(self, courseID):
                return redirect("manage_course")
        return render(request, '403.html', {})


class CreateCourse(View):
    def get(self, request):
        if isLoggedIn(request.session):
            return render(request, 'create_course.html', {})
        return render(request, '403.html', {})

    def post(self, request):
        if isLoggedIn(request.session):
            input_name = request.POST.get('input_name')
            input_credit = request.POST.get('input_credit')

            if len(input_name) < 3 or len(input_name) > 30 :
                return render(request, 'create_course.html', {"message": "ERROR: invalid name length, try gain."})
            elif int(input_credit) < 1 or len(input_credit) > 10:
                return render(request, 'create_course.html', {"message": "ERROR: invalid credit, try gain."})
            else:
                toAdd = Course(name=input_name, credit=input_credit)
                if CourseClass.CourseClass.addCourse(self, toAdd):
                    return render(request, 'create_course.html', {"message": "SUCCESS! Course added successfully."})
        return render(request, '403.html', {})

