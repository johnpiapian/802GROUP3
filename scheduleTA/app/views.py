from django.shortcuts import render, redirect
from django.views import View
from classes import UserClass, CourseClass, ClassClass
from .models import User, Course, Class


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


def isProfessorLoggedIn(session):
    if isLoggedIn(session):
        # check if the logged-in user has admin role
        if UserClass.UserClass.getRole(None, session['name']) == 'P':
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
        fullForm = {'A': "Admin", 'P': "Professor", 'T': "TA"}
        # handle unauthorized access by redirecting them to the login page
        if isLoggedIn(request.session):
            name = request.session["name"]
            role = UserClass.UserClass.getRole(self, name)
            return render(request, "homepage_0.html", {"name": name, "role": fullForm.get(role)})
        return redirect("home")


class CreateUser(View):
    def get(self, request):
        # handle unauthorized access by showing them 403 error
        if isAdminLoggedIn(request.session):
            return render(request, "create_user.html", {})
        elif isLoggedIn(request.session):
            return render(request, '403.html', {}, status=403)
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
        return render(request, '403.html', {}, status=403)


class ViewUser(View):
    def get(self, request):
        # handle unauthorized access by showing them 403 error
        if isAdminLoggedIn(request.session):
            return render(request, 'view_user.html', {"users": UserClass.UserClass.getAllUsers(self)})
        return render(request, '403.html', {}, status=403)


class ViewUserSingle(View):
    def get(self, request, name):
        # handle unauthorized access by showing them 403 error
        if isAdminLoggedIn(request.session):
            return render(request, 'view_user_single.html',
                          {"type": "admin", "user": UserClass.UserClass.getUser(self, name)})
        return render(request, '403.html', {}, status=403)


class UpdateUser(View):
    def post(self, request):
        # handle unauthorized access by showing them 403 error
        if isLoggedIn(request.session):
            input_id = request.POST.get('input_id')
            input_name = request.POST.get('input_name')
            input_pw1 = request.POST.get('input_pw1')
            input_pw2 = request.POST.get('input_pw2')
            input_role = request.POST.get('input_role')
            input_skills = request.POST.get('input_skills')
            roles = ['A', 'P', 'T']

            # Need it for certain session management
            oldName = UserClass.UserClass.getUserByID(self, int(input_id)).name

            # non admin should be able to update only their profile
            if oldName != request.session['name'] and not isAdminLoggedIn(request.session):
                return render(request, '403.html', {}, status=403)

            if len(input_pw1) > 0 and input_pw1 != input_pw2:
                return render(request, "base-error.html",
                              {"message": "ERROR: Passwords do NOT match, try again.", "url": "view_user"})
            elif input_role is not None and input_role not in roles:
                return render(request, "base-error.html",
                              {"message": "ERROR: invalid input role type, try again.", "url": "view_user"})
            else:
                userToUpdate = User(id=int(input_id), name=input_name, password=input_pw1, role=input_role,
                                    skills=input_skills)
                if UserClass.UserClass.updateUser(self, userToUpdate):
                    # update session name if we are updating self
                    if request.session['name'] == oldName:
                        request.session['name'] = input_name

                    if isAdminLoggedIn(request.session):
                        return redirect("view_user")
                    else:
                        return redirect("homepage_0")

        return render(request, '403.html', {}, status=403)


class DeleteUser(View):
    def post(self, request):
        # handle unauthorized access
        if isLoggedIn(request.session):
            input_id = request.POST.get('input_id')
            input_name = request.POST.get('input_name')

            # non-admin user should only be able to delete their profile
            if input_name != request.session['name'] and not isAdminLoggedIn(request.session):
                return render(request, '403.html', {}, status=403)

            if UserClass.UserClass.getUser(self, input_name).id == int(input_id) and UserClass.UserClass.deleteUser(
                    self, input_name):
                if request.session['name'] == input_name:
                    return redirect("logout")
                return redirect("view_user")
        return render(request, '403.html', {}, status=403)


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
        return render(request, '403.html', {}, status=403)


class Logout(View):
    def get(self, request):
        if isLoggedIn(request.session):
            del request.session["name"]
            return redirect("home")
        return render(request, 'base-error.html', {"title": "Unexpected error!"})


# Course
class ManageCourse(View):
    def get(self, request):
        if isAdminLoggedIn(request.session):
            return render(request, 'manage_course.html', {"courses": CourseClass.CourseClass.getAllCourses(self)})
        return render(request, '403.html', {}, status=403)


class DeleteCourse(View):
    def get(self, request, courseID):
        if isLoggedIn(request.session):
            if CourseClass.CourseClass.deleteCourse(self, courseID):
                return redirect("manage_course")
        return render(request, '403.html', {}, status=403)


class CreateCourse(View):
    def get(self, request):
        if isLoggedIn(request.session) and isAdminLoggedIn(request.session):
            return render(request, 'create_course.html', {})
        return render(request, '403.html', {}, status=403)

    def post(self, request):
        if isLoggedIn(request.session) and isAdminLoggedIn(request.session):
            input_name = request.POST.get('input_name')
            input_credit = request.POST.get('input_credit')

            if len(input_name) < 3 or len(input_name) > 30:
                return render(request, 'create_course.html', {"message": "ERROR: invalid name length, try gain."})
            elif int(input_credit) < 1 or len(input_credit) > 10:
                return render(request, 'create_course.html', {"message": "ERROR: invalid credit, try gain."})
            else:
                toAdd = Course(name=input_name, credit=input_credit)
                if CourseClass.CourseClass.addCourse(self, toAdd):
                    return render(request, 'create_course.html', {"message": "SUCCESS! Course added successfully."})
        return render(request, '403.html', {}, status=403)


class CreateClass(View):
    def get(self, request):
        if isLoggedIn(request.session):
            if isAdminLoggedIn(request.session) or isProfessorLoggedIn(request.session):
                return render(request, 'create_class.html', {"courses": CourseClass.CourseClass.getAllCourses(self),
                                                             "users": UserClass.UserClass.getAllUsers(self)})
            else:
                return render(request, '403.html', {}, status=403)
        return redirect('homepage_0')

    def post(self, request):
        if isAdminLoggedIn(request.session) or isProfessorLoggedIn(request.session):
            course = request.POST.get('course')
            class_number = request.POST.get('class_number')
            room_number = request.POST.get('room_number')
            teacher_name = request.POST.get('teacher')
            type = request.POST.get('class_type')
            start_time = request.POST.get('start_time')
            end_time = request.POST.get('end_time')

            toAdd = Class(course=CourseClass.CourseClass.getCourse(self, course), class_number=class_number,
                          room_number=room_number, teacher_name=UserClass.UserClass.getUser(self, teacher_name),
                          class_type=type,
                          start_time=start_time, end_time=end_time)
            if ClassClass.ClassClass.addClass(self, toAdd) == True:
                return render(request, 'create_class.html', {"message": "SUCCESS! Class added successfully.",
                                                             "courses": CourseClass.CourseClass.getAllCourses(self),
                                                             "users": UserClass.UserClass.getAllUsers(self)})
            else:
                return render(request, 'create_class.html', {"message": "Class already exists",
                                                             "courses": CourseClass.CourseClass.getAllCourses(self),
                                                             "users": UserClass.UserClass.getAllUsers(self)})
        return render(request, '403.html', {}, status=403)


class ManageClasses(View):
    def get(self, request):
        if isAdminLoggedIn(request.session):
            return render(request, 'manage_classes.html', {"classes": ClassClass.ClassClass.getAllClasses(self),
                                                           "users": UserClass.UserClass.getAllUsers(self)})
        elif isProfessorLoggedIn(request.session):
            return render(request, 'manage_classes.html', {"classes": UserClass.UserClass.getUserClasses(self,
                                                                                                         UserClass.UserClass.getUser(
                                                                                                             self,
                                                                                                             request.session[
                                                                                                                 'name'])),
                                                           "users": UserClass.UserClass.getAllUsers(self)})
        return render(request, '403.html', {}, status=403)

    def post(self, request):
        if isAdminLoggedIn(request.session):
            teacher_name = request.POST.get('teacher')
            update_class_number = request.POST.get('update_class_number')
            class_to_be_updated = Class.objects.get(class_number=update_class_number)
            class_to_be_updated.teacher_name = UserClass.UserClass.getUser(self, teacher_name)
            class_to_be_updated.save()
            return render(request, 'manage_classes.html', {"classes": ClassClass.ClassClass.getAllClasses(self),
                                                           "users": UserClass.UserClass.getAllUsers(self)})
        if isLoggedIn(request.session):
            teacher_name = request.POST.get('teacher')
            update_class_number = request.POST.get('update_class_number')
            class_to_be_updated = Class.objects.get(class_number=update_class_number)
            if class_to_be_updated.teacher_name.name == request.session['name']:
                return render(request, 'manage_classes.html', {"classes": UserClass.UserClass.getUserClasses(self,
                                                                                                             UserClass.UserClass.getUser(
                                                                                                                 self,
                                                                                                                 request.session[
                                                                                                                     'name'])),
                                                               "users": UserClass.UserClass.getAllUsers(self),
                                                               "message": "ERROR: Cannot remove self from Class, speak to an Admin."})
            else:
                class_to_be_updated.teacher_name = UserClass.UserClass.getUser(self, teacher_name)
                class_to_be_updated.save()
                return render(request, 'manage_classes.html', {"classes": UserClass.UserClass.getUserClasses(self,
                                                                                                             UserClass.UserClass.getUser(
                                                                                                                 self,
                                                                                                                 request.session[
                                                                                                                     'name'])),
                                                               "users": UserClass.UserClass.getAllUsers(self),
                                                               "message": "SUCCESS: Teacher/TA updated!"})
        return render(request, '403.html', {}, status=403)


class DeleteClass(View):
    def get(self, request, classID):
        if isLoggedIn(request.session):
            if ClassClass.ClassClass.deleteClass(self, classID):
                return redirect("manage_classes")
        return render(request, '403.html', {}, status=403)
