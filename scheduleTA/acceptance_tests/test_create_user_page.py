from django.test import TestCase, Client
##need to import user models once they are implemented.
from app.models import User

class newUser(TestCase):

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

    def test_nonAdminUser(self):
        # if session user is not admin redirect to homepage
        session = self.client.session
        session['roll'] = "TA"
        session.save()
        resp = self.mockUser.get("/createUser/", follow=True)
        self.assertTemplateUsed(resp, 'homePage.html')

    def test_userNameTaken(self):
        for i in self.userList:
            resp = self.mockUser.post("/createUser/", {"name": i.name(), "password": "pass", "role": "A"}, follow=True)
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
        # might want to check that the user has been added to the database as well

    def test_badPassword(self):
        # If we want to add requirements to password strength will need to implement.
        pass
