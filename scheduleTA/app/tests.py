from django.test import TestCase, Client
##need to import user models once they are implemented.
from .models import User


# Create your tests here.


class Login(TestCase):
    mockUser = None
    userList = None

    def setUp(self):
        # set up database for tests
        self.mockUser = Client()
        self.userList = {"admin": "password", "colin": "1234", "user": "Password"}
        for key in self.userList:
            # will need to change to fit implemented models
            User(role=3, username=key, password=self.userList[key]).save()

    def test_incorrectPassword(self):
        for key in self.userList:
            resp = self.mockUser.post("/", {"name": key, "password": "a"}, follow=True)
            self.assertEqual(resp.context["message"], "bad Password", "Password is incorrect")

    def test_noPassword(self):
        for key in self.userList:
            resp = self.mockUser.post("/", {"name": key, "password": ""}, follow=True)
            self.assertEqual(resp.context["message"], "bad password", "Password is incorrect")

    def test_noSuchUser(self):

        for key in self.userList:
            resp = self.mockUser.post("/", {"name": "a", "password": self.userList[key]}, follow=True)
            self.assertEqual(resp.context["message"], "No user found", "no such user")

    def test_goodLoggin(self):
        for key in self.userList:
            resp = self.mockUser.post("/", {"name": key, "password": self.userList[key]}, follow=True)
            # confirm we are taken to homepage.


class newUser(TestCase):

    def setUp(self):
        def setUp(self):
            # set up database for tests
            self.mockUser = Client()
            self.userList = {"admin": "password", "colin": "1234", "user": "Password"}

            for key in self.userList:
                # will need to change to fit implemented models
                User(role=2, username=key, password=self.userList[key]).save()

    def test_nonAdminUser(self):
        #if session user is not admin redirect to homepage
        session = self.client.session
        session['roll'] = "TA"
        session.save()
        resp = self.mockUser.get("/createUser/", follow = True)
        self.assertTemplateUsed(resp, 'homePage.html')
        

    def test_userNameTaken(self):
        for key in self.userList:
            resp = self.mockUser.post("/createUser/", {"name": key, "password": "pass", "role": "A"}, follow=True)
            self.assertEqual(resp.context["message"], "User already exists", "user name taken")

    def test_noPassword(self):
        resp = self.mockUser.post("/createUser/", {"name": "test", "password": "", "role": "A"}, follow=True)
        self.assertEqual(resp.context["message"], "needs password", "no password entered")

    def test_noUserName(self):
        resp = self.mockUser.post("/createUser/", {"name": "", "password": "1234", "role": "A"}, follow=True)
        self.assertEqual(resp.context["message"], "needs a user name", "no user name")

    def test_UserCreated(self):
        resp = self.mockUser.post("/createUser/", {"name": "newUser", "password": "abc", "role": "A"}, follow=True)
        self.assertEqual(resp.context["message"], "Created new user", "created new user")
        #might want to check that the user has been added to the database as well

    def test_badPassword(self):
        # If we want to add requirements to password strength will need to implement.
        pass
