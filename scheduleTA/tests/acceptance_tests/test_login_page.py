from tests import test_SetUp

class Login(test_SetUp.dbSetup):

    def setUp(self):
        super().setUp()
    def test_incorrectPassword(self):
        for i in self.userList:
            resp = self.mockUser.post("/", {"name": i.name, "password": "a"}, follow=True)
            self.assertEqual(resp.context["message"],"Login Error: Invalid password, try again.")

    def test_noPassword(self):
        for i in self.userList:
            resp = self.mockUser.post("/", {"name": i.name, "password": ""}, follow=True)
            self.assertEqual(resp.context["message"],"Login Error: Invalid password, try again.")

    def test_noSuchUser(self):

        for i in self.userList:
            resp = self.mockUser.post("/", {"name": "a", "password": i.password}, follow=True)
            self.assertEqual(resp.context["message"], 'Login Error: Invalid username, try again.')

    def test_goodLoggin(self):
        for i in self.userList:
            resp = self.mockUser.post("/", {"name": i.name, "password": i.password}, follow=True).redirect_chain
            self.assertEqual(resp,[('/homepage_0/',302)])

