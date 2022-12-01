
##need to import user models once they are implemented.

from tests import test_SetUp

# Create your tests here.


class Login(test_SetUp.UserList):

    def setUp(self):
        super().setUp()
    def test_incorrectPassword(self):
        for i in self.userList:
            resp = self.mockUser.post("/", {"name": i.name, "password": "a"}, follow=True)
            self.assertEqual(resp.context["message"],"Password is incorrect")

    def test_noPassword(self):
        for i in self.userList:
            resp = self.mockUser.post("/", {"name": i.name, "password": ""}, follow=True)
            self.assertEqual(resp.context["message"],"Password is incorrect")

    def test_noSuchUser(self):

        for i in self.userList:
            resp = self.mockUser.post("/", {"name": "a", "password": i.password}, follow=True)
            self.assertEqual(resp.context["message"], 'UserName is incorrect')

    def test_goodLoggin(self):
        for i in self.userList:
            resp = self.mockUser.post("/", {"name": i.name, "password": i.password}, follow=True)
            self.assertEqual(resp.url,'homepage_0/')

