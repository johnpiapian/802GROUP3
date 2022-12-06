from tests import test_SetUp

class newUser(test_SetUp.dbSetup):

    def setUp(self) -> None:
        super().setUp()

    def test_nonAdminUser(self):
        # if session user is not admin redirect to homepage
        session = self.client.session
        session['roll'] = "TA"
        session.save()
        resp = self.mockUser.get("/create_user/", follow=True)
        self.assertEqual(resp,[('/homepage_0/',302)])

    def test_userNameTaken(self):
        for i in self.userList:
            resp = self.mockUser.post("/create_user/", {"name": i.name, "password": "pass", "role": "A"}, follow=True)
            self.assertEqual(resp.context["message"], "ERROR: Username already exists in database, try again.")

    def test_noPassword(self):
        resp = self.mockUser.post("/create_user/", {"name": "test", "password": "", "role": "A"}, follow=True)
        self.assertEqual(resp.context["message"], "needs password")

    def test_noUserName(self):
        resp = self.mockUser.post("/create_user/", {"name": "", "password": "1234", "role": "A"}, follow=True)
        self.assertEqual(resp.context["message"], "needs a user name")

    def test_UserCreated(self):
        resp = self.mockUser.post("/create_user/", {"name": "newUser", "password": "abc", "role": "A"}, follow=True)
        self.assertEqual(resp.context["message"], "SUCCESS! User added successfully.")
        # might want to check that the user has been added to the database as well

    def test_badPassword(self):
        # If we want to add requirements to password strength will need to implement.
        pass
