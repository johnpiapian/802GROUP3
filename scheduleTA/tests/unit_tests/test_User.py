from classes import UserClass
from tests import test_SetUp
class UserUnitTests(test_SetUp.dbSetup):
    def setUp(self):
        super().setUp()

    def test_userExists_00(self):
        for i in self.userList:
            self.assertEqual(True, UserClass.UserClass.userExists(self, i.name), "lol you failed")
            self.assertEqual(True, UserClass.UserClass.userExists(self, i.name.upper()), "lol you failed")
    def test_userExists_01(self):
        self.assertEqual(False, UserClass.UserClass.userExists(self, ''))
    def test_userExists_02(self):
        self.assertEqual(False, UserClass.UserClass.userExists(self, 'A'))
    def test_userExists_03(self):
        self.assertEqual(False, UserClass.UserClass.userExists(self, 1234))
    def test_getUser_00(self):
        for i in self.userList:
            self.assertEqual(i, UserClass.UserClass.getUser(self, i.name))
            self.assertEqual(i, UserClass.UserClass.getUser(self, i.name.upper()))
    def test_getUser_01(self):
        self.assertEqual(None, UserClass.UserClass.getUser(self, ''))
    def test_getUser_02(self):
        self.assertEqual(None, UserClass.UserClass.getUser(self, 'A'))
    def test_getUser_03(self):
        self.assertEqual(None, UserClass.UserClass.getUser(self, 1234))

    def test_addUser(self):
        self.assertEqual(True, UserClass.addUser(['A','John','Test']))
        self.assertEqual(False, UserClass.addUser(['A', 'Colin', 'Test']))
        self.assertEqual(False, UserClass.addUser(['P', 'Colin', '1234']))
        self.assertEqual(False, UserClass.addUser( ['A', 'CoLiN', '1234']))

    def test_updateUser(self):
        self.assertEqual(True, UserClass.updateUser(['A','Colin','newPassword']))
        self.assertEqual(False, UserClass.updateUser(['A','Colin','newPassword']))
        self.assertEqual(True, UserClass.updateUser(['T','Colin','newPassword']))
        self.assertEqual(False, UserClass.updateUser( ['A','Colin','']))
        self.assertEqual(False, UserClass.updateUser(['','Colin','newPassword']))
        self.assertEqual(False, UserClass.updateUser(['A','asdjksdjkdsf','newPassword']))


    def test_deleteUser(self):
        self.assertContains(self.userList,self.Colin)
        self.assertEqual(True, UserClass.deleteUser('colin'))
        self.assertNotContains(self.userList, self.Colin)
        self.assertEqual(False,UserClass.deleteUser('colin'))
        self.assertEqual(False, UserClass.deleteUser(''))
