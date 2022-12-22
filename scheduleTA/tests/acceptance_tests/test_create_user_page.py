from tests import test_SetUp

class newUser(test_SetUp.dbSetup):

    def setUp(self) -> None:
        super().setUp()

    def test_nonAdminUser(self):
        # if session user is not admin redirect to homepage
        session = self.mockUser.session
        session['name'] = "joe"
        session.save()
        resp = self.mockUser.get("/create_user/", follow=True)
        self.assertEqual(resp.status_code, 403)

    def test_userNameTaken(self):
        for i in self.userList:
            resp = self.mockUser.post("/create_user/", {"name": i.name, "password": "pass", "role": "A"}, follow=True)
            self.assertEqual(resp.context["message"], "ERROR: Username already exists in database, try again.")

    def test_noPassword(self):
        session = self.mockUser.session
        session['name'] = "admin"
        session['role'] = "T"
        session.save()
        resp = self.mockUser.post("/create_user/", {"name": "test", "password": "", "role": "A"}, follow=True)
        self.assertEqual(resp.context["message"], "needs password")

    def test_noUserName(self):
        resp = self.mockUser.post("/create_user/", {"name": "", "password": "1234", "role": "A"}, follow=True)
        self.assertEqual(resp.context["message"], "needs a user name")

    def test_UserCreated(self):
        session = self.mockUser.session
        session['name'] = "Test"
        session['role'] = "A"
        session.save()
        resp = self.mockUser.post("/create_user/", {"input_name": "newUser", "input_pw1": "abc", "input_role": "A"}, follow=True)
        print(resp.context[''])
        # might want to check that the user has been added to the database as well

    def test_badPassword(self):
        # If we want to add requirements to password strength will need to implement.
        pass
