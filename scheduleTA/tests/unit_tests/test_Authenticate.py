from classes import AuthenticateClass
from tests import test_SetUp


class AuthenticateTest(test_SetUp.dbSetup):

    def setUp(self):
        super().setUp()

    def test_login(self):
        for i in self.userList:
            self.assertEqual(True, AuthenticateClass.login([i.name,i.password]))
            self.assertEqual(True, AuthenticateClass.login([i.name.lower(),i.password]))
            self.assertEqual(False, AuthenticateClass.login([i.name,'']))
            self.assertEqual(False, AuthenticateClass.login(['',i.password]))
    def test_logout(self):
        session = self.client.session
        session['user'] = self.Colin
        session.save()
        self.assertEqual(True, AuthenticateClass.logout())
        self.assertEqual(None, session['user'])
        self.assertEqual(False,AuthenticateTest.logout())

