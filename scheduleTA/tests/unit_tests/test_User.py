
from classes import UserClass
from tests import test_SetUp
class UserUnitTests(test_SetUp):

    def setUp(self):
        super().setUp()

    def test_userExists(self):
        for i in self.userList:
            self.assertEqual(True, UserClass.userExists(i.name))
            self.assertEqual(True, UserClass.userExists(i.name.upper()))
        self.assertEqual(False,UserClass.userExists(''))
        self.assertEqual(False,UserClass.userExists('A'))
        self.assertEqual(False,UserClass.userExists(1234))
    def test_getUser(self):
        for i in self.userList:
            self.assertEqual(i,UserClass.getUser(i.name))
            self.assertEqual(i,UserClass.getUser(i.name.upper()))
        self.assertEqual(None, UserClass.getUser(''))
        self.assertEqual(None,UserClass.getUser('A'))
        self.assertEqual(None, UserClass.getUser(1234))

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
