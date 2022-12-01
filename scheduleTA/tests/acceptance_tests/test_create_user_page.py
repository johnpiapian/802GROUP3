
##need to import user models once they are implemented.

from tests import test_SetUp

class newUser(test_SetUp.UserList):

    def setUp(self) -> None:
        super().setUp()

    def test_nonAdminUser(self):
        # if session user is not admin redirect to homepage
        session = self.client.session
        session['roll'] = "TA"
        session.save()
        resp = self.mockUser.get("/createUser/", follow=True)
        self.assertTemplateUsed(resp.url, 'homepage_0/')

    def test_userNameTaken(self):
        for i in self.userList:
            resp = self.mockUser.post("/createUser/", {"name": i.name, "password": "pass", "role": "A"}, follow=True)
            self.assertEqual(resp.context["message"], "User already exists")

    def test_noPassword(self):
        resp = self.mockUser.post("/createUser/", {"name": "test", "password": "", "role": "A"}, follow=True)
        self.assertEqual(resp.context["message"], "needs password")

    def test_noUserName(self):
        resp = self.mockUser.post("/createUser/", {"name": "", "password": "1234", "role": "A"}, follow=True)
        self.assertEqual(resp.context["message"], "needs a user name")

    def test_UserCreated(self):
        resp = self.mockUser.post("/createUser/", {"name": "newUser", "password": "abc", "role": "A"}, follow=True)
        self.assertEqual(resp.context["message"], "Created new user")
        # might want to check that the user has been added to the database as well

    def test_badPassword(self):
        # If we want to add requirements to password strength will need to implement.
        pass
