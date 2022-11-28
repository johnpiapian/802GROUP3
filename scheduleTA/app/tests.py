from django.test import TestCase, Client
##need to import user models once they are implemented.

# Create your tests here.


class LoginFail(TestCase):
    user = None
    userList = None

    def setUp(self):
        #set up database for tests
        self.user = Client()
        self.userList = {"admin" :"password", "colin" :"1234", "user" :"Password"}
        i = 0
        for key in self.userList:

            #will need to change to fit implemented models
            MyUser(id=i, role = 3, username=key,password=self.userList[key]).save()
            i+=1

    def test_incorrectPassword(self):
        for key in self.userList:
            resp = self.user.post("/",{"name":key, "password":"a"}, follow = True)
            self.assertEqual(resp.context["password"],self.userList[key],"Password is incorrect")

    def test_noPassword(self):
        for key in self.userList:
            resp = self.user.post("/",{"name":key,"password" : ""}, follow = True)
            self.assertEqual(resp.context["password"],self.userList[key], "Password is incorrect")


    def test_noSuchUser(self):

        for key in self.userList:
            resp = self.user.post("/", {"name":"a","password":self.userList[key]},follow = True)
            self.assertEqual(resp.context["name"],"a", "no such user")

    def test_goodLoggin(self):
        for key in self.userList:
            resp = self.user.post("/", {"name":key,"password":self.userList[key]},follow = True)
            #confirm we are taken to homepage.

class newUser(TestCase):

    def setUp(self):
        pass

    def test_nonAdminUser(self):
        pass

    def test_userNameTaken(self):
        pass

    def test_noPassword(self):
        pass

    def test_noUserName(self):
        pass

    def test_badPassword(self):
        pass
