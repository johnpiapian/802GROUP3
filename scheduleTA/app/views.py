from django.shortcuts import render
from django.views import View


# Create your views here.
class Home(View):
    def get(self, req):
        return render(req, "index.html", {})

    def post(self, req):
        return render(req, "index.html", {})
