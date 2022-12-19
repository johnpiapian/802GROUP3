from classes import UserClass
from tests import test_SetUp
class UserUnitTests(test_SetUp.dbSetup):
    def setUp(self):
        super().setUp()

    def test_userExists_00(self):
        for i in self.userList:
            self.assertEqual(True, UserClass.UserClass.userExists(self, i.name))
            self.assertEqual(True, UserClass.UserClass.userExists(self, i.name.upper()))
            self.assertEqual(True, UserClass.UserClass.userExists(self, i.name.lower()))
    def test_userExists_01(self):
        self.assertEqual(False, UserClass.UserClass.userExists(self, ''))
    def test_userExists_02(self):
        self.assertEqual(False, UserClass.UserClass.userExists(self, 'A'))
    def test_userExists_03(self):
        self.assertEqual(False, UserClass.UserClass.userExists(self, None))
    def test_getUser_00(self):
        for i in self.userList:
            self.assertEqual(i, UserClass.UserClass.getUser(self, i.name))
            self.assertEqual(i, UserClass.UserClass.getUser(self, i.name.upper()))

    def test_getUser_01(self):
        self.assertEqual(None, UserClass.UserClass.getUser(self, ''))
    def test_getUser_02(self):
        self.assertEqual(None, UserClass.UserClass.getUser(self, 'A'))
    def test_getUser_03(self):
        self.assertEqual(None, UserClass.UserClass.getUser(self, None))

    def test_addUser_00(self):
        self.assertEqual(True, UserClass.UserClass.addUser(self, self.Lisa))
    def test_addUser_01(self):
        self.assertEqual(False, UserClass.UserClass.addUser(self,self.Colin))
    def test_addUser_02(self):
        self.assertEqual(False, UserClass.UserClass.addUser(self, self.ColinPchange))
    def test_addUser_03(self):
        self.assertEqual(False, UserClass.UserClass.addUser(self, self.ColinRchange))

    def test_updateUser_00(self):
        self.Colin.password = "newPassword!"
        self.assertEqual(True, UserClass.UserClass.updateUser(self, self.Colin))
        #self.assertEqual(True, UserClass.UserClass.updateUser(self, self.ColinPchange))
    def test_updateUser_01(self):
        self.assertEqual(False, UserClass.UserClass.updateUser(self, self.Colin))
    def test_updateUser_02(self):
        self.Colin.role = "T"
        self.assertEqual(True, UserClass.UserClass.updateUser(self, self.Colin))
        #self.assertEqual(True, UserClass.UserClass.updateUser(self, self.ColinRchange))
    def test_updateUser_03(self):
        self.ColinPchange.password = ''
        self.assertEqual(False, UserClass.UserClass.updateUser(self, self.ColinPchange))
    def test_updateUser_04(self):
        self.ColinRchange.role = ''
        self.assertEqual(False, UserClass.UserClass.updateUser(self, self.ColinRchange))
    def test_updateUser_05(self):
        self.assertEqual(False, UserClass.UserClass.updateUser(self, self.Lisa))

    def test_getRole_00(self):
        self.assertEqual('A', UserClass.UserClass.getRole(self,self.Colin.name))
    def test_getRole_01(self):
        self.assertEqual(None, UserClass.UserClass.getRole(self,'Randy'))
    def test_getRole_02(self):
        self.assertEqual(None, UserClass.UserClass.getRole(self,''))
    def test_getRole_03(self):
        self.assertEqual(None, UserClass.UserClass.getRole(self,None))



    def test_deleteUser_00(self):
        self.assertEqual(True, self.userList.contains(self.Colin))
    def test_deleteUser_01(self):
        self.assertEqual(True, UserClass.UserClass.deleteUser(self,'Colin'))
    def test_deleteUser_02(self):
        self.assertEqual(False, UserClass.UserClass.deleteUser(self, ''))
    def test_deleteUser_03(self):
        self.assertEqual(False, UserClass.UserClass.deleteUser(self, 'NameNotInDatabase'))