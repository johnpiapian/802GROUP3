from classes import UserClass
from tests import test_SetUp
class UserUnitTests(test_SetUp.dbSetup):
    def setUp(self):
        super().setUp()

    def test_userExists_00(self):
        for i in self.userList:
            self.assertEqual(True, UserClass.UserClass.userExists(self, i.name), "lol you failed")
            self.assertEqual(True, UserClass.UserClass.userExists(self, i.name.upper()), "lol you failed")
            self.assertEqual(True, UserClass.UserClass.userExists(self, i.name.lower()), "lol you failed")
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

    def test_passwordCorrect_00(self):
        self.assertEqual(True, UserClass.UserClass.passwordCorrect(self,self.Colin,'1234'))
    def test_passwordCorrect_01(self):
        self.assertEqual(False, UserClass.UserClass.passwordCorrect(self,self.Admin,'1234'))
    def test_passwordCorrect_02(self):
        self.assertEqual(True, UserClass.UserClass.passwordCorrect(self,self.Colin,1234))
    def test_passwordCorrect_03(self):
        self.assertEqual(False, UserClass.UserClass.passwordCorrect(self,self.Admin,'pAsSwOrD'))
    def test_passwordCorrect_04(self):
        self.assertEqual(False, UserClass.UserClass.passwordCorrect(self, self.Admin, ''))
    def test_passwordCorrect_05(self):
        self.assertEqual(False, UserClass.UserClass.passwordCorrect(self, None, '1234'))


    def test_getUser_01(self):
        self.assertEqual(None, UserClass.UserClass.getUser(self, ''))
    def test_getUser_02(self):
        self.assertEqual(None, UserClass.UserClass.getUser(self, 'A'))
    def test_getUser_03(self):
        self.assertEqual(None, UserClass.UserClass.getUser(self, None))

    def test_addUser_00(self):
        self.assertEqual(True, UserClass.UserClass.addUser(self, ['A','John','Test']))
    def test_addUser_01(self):
        self.assertEqual(False, UserClass.UserClass.addUser(self,['A', 'Colin', 'Test']))
    def test_addUser_02(self):
        self.assertEqual(False, UserClass.UserClass.addUser(self, ['P', 'Colin', '1234']))
    def test_addUser_03(self):
        self.assertEqual(False, UserClass.UserClass.addUser(self, ['A', 'CoLiN', '1234']))

    def test_updateUser_00(self):
        self.assertEqual(True, UserClass.UserClass.updateUser(self, ['A','Colin','newPassword']))
    def test_updateUser_01(self):
        self.assertEqual(False, UserClass.UserClass.updateUser(self, ['A','Colin','newPassword']))
    def test_updateUser_02(self):
        self.assertEqual(True, UserClass.UserClass.updateUser(self, ['T','Colin','newPassword']))
    def test_updateUser_03(self):
        self.assertEqual(False, UserClass.UserClass.updateUser(self, ['A','Colin','']))
    def test_updateUser_04(self):
        self.assertEqual(False, UserClass.UserClass.updateUser(self, ['','Colin','newPassword']))
    def test_updateUser_05(self):
        self.assertEqual(False, UserClass.UserClass.updateUser(self, ['A','asdjksdjkdsf','newPassword']))

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
        self.assertEqual(False, UserClass.UserClass.deleteUser(self, 'Colin'))
    def test_deleteUser_02(self):
        self.assertEqual(False, UserClass.UserClass.deleteUser(self, ''))
