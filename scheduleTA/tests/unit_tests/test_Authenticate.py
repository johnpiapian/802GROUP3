from classes import AuthenticateClass
from tests import test_SetUp


class AuthenticateTest(test_SetUp.dbSetup):

    def setUp(self):
        super().setUp()

    def test_login(self):
        for i in self.userList:
            self.assertEqual(True, AuthenticateClass.Authenticate.login(self,[i.name,i.password]))
            self.assertEqual(True, AuthenticateClass.Authenticate.login(self,[i.name.lower(),i.password]))
            self.assertEqual(False, AuthenticateClass.Authenticate.login(self,[i.name,'']))
            self.assertEqual(False, AuthenticateClass.Authenticate.login(self,['',i.password]))
    def test_logout(self):
        session = self.client.session
        session['user'] = self.Colin
        session.save()
        self.assertEqual(True, AuthenticateClass.Authenticate.logout(self))
        self.assertEqual(None, session['user'])
        self.assertEqual(False,AuthenticateClass.Authenticate.logout(self))

