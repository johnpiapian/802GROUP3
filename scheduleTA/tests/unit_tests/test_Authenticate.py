from classes import AuthenticateClass
from tests import test_SetUp


class AuthenticateTest(test_SetUp.dbSetup):

    def setUp(self):
        super().setUp()


    def test_validateName_00(self):
        user = AuthenticateClass.Authenticate('Colin','1234')
        self.assertEqual(True, user.validateName())
    def test_validateName_01(self):
        user = AuthenticateClass.Authenticate('', '1234')
        self.assertEqual(False, user.validateName())
    def test_validateName_03(self):
        user = AuthenticateClass.Authenticate('djsdfjfdsjkdfsjklsdfkjlfdsalkjsdflkjsdfalkjfljkdfslkjfs','1234')
        self.assertEqual(False, user.validateName())
    def test_validateName_04(self):
        user = AuthenticateClass.Authenticate(1234,'1234')
        self.assertEqual(True, user.validateName())

    def test_validatePassword_00(self):
        user = AuthenticateClass.Authenticate('Colin','1234')
        self.assertEqual(True, user.validatePassword())
    def test_validatePassword_01(self):
        user = AuthenticateClass.Authenticate('Colin','')
        self.assertEqual(False, user.validatePassword())
    def test_validatePassword_02(self):
        user = AuthenticateClass.Authenticate('Colin','ajkldsfjasdlkfjdslkfjsdalkfjsdaklfjadsfasdfds')
        self.assertEqual(False, user.validatePassword())
    def test_validatePassword_03(self):
        user = AuthenticateClass.Authenticate('Colin',1234)
        self.assertEqual(True, user.validatePassword())

    def test_validateUser_00(self):
        for i in self.userList:
            user = AuthenticateClass.Authenticate(i.name,i.password)
            self.assertEqual(False, user.validateUser())