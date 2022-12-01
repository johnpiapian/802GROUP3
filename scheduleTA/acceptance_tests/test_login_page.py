from django.test import TestCase, Client
##need to import user models once they are implemented.
from app.models import User


# Create your tests here.


class Login(TestCase):
    mockUser = None
    userList = None

    def setUp(self):
        # set up database for tests
        self.mockUser = Client()

        self.Admin = User.objects.create(role='A', name='Admin1!', password='Password')
        self.Colin = User.objects.create(role='A', name='Colin', password='1234')
        self.George = User.objects.create(role='T', name='George', password="1234")
        self.Humraj = User.objects.create(role='T', name='Humraj', password='pAsSwOrD')
        self.Nicholas = User.objects.create(role='P', name='Nicholas', password='a!2/}')
        self.Sut = User.objects.create(role='P', name='Sut', password='abcd')

        self.userList = User.objects.all()
    def test_incorrectPassword(self):
        for i in self.userList:
            resp = self.mockUser.post("/", {"name": i.name(), "password": "a"}, follow=True)
            self.assertEqual(resp.context["message"], "bad Password", "Password is incorrect")

    def test_noPassword(self):
        for i in self.userList:
            resp = self.mockUser.post("/", {"name": i.name(), "password": ""}, follow=True)
            self.assertEqual(resp.context["message"], "bad password", "Password is incorrect")

    def test_noSuchUser(self):

        for i in self.userList:
            resp = self.mockUser.post("/", {"name": "a", "password": i.password}, follow=True)
            self.assertEqual(resp.context["message"], "No user found", "no such user")

    def test_goodLoggin(self):
        for i in self.userList:
            resp = self.mockUser.post("/", {"name": i.name(), "password": i.password()}, follow=True)
            # confirm we are taken to homepage.

