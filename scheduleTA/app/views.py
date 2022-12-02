from django.shortcuts import render, redirect
from django.views import View
from .models import User, Course, Section


# Create your views here.
class Home(View):
    def get(self, request):
        return render(request, 'home.html', {})
    def post(self, request):
        no_such_user = False
        bad_password = False
        try:
            # Goto User database, get object name = 'name'
            m = User.objects.get(name=request.POST['name'])
            bad_password = (m.password != request.POST['password'])
        except:
            # if above code fails, user doesn't exist, set the boolean
            no_such_user = True
        if no_such_user:
            return render(request, 'home.html', {"message":"Login Error: Invalid username, try again."})
        elif bad_password:
            return render(request, 'home.html', {"message":"Login Error: Invalid password, try again."})
        else:
            request.session["name"] = m.name
            return redirect("homepage_0")

class Homepage_0(View):
    def get(self, request):
        m = request.session["name"]
        role = User.objects.filter(name=m).values_list('role',flat=True)
        return render(request, "homepage_0.html", {"name":m,"role":role})