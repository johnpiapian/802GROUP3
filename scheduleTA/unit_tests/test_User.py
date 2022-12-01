from django.test import TestCase
from app.models import User
from classes import UserClass

class LoginUnitTests(TestCase):

    def test_role(self):
        user = UserClass('A', 'Colin', 'abcd')
        self.assertEqual('A', user.roll)
        user = UserClass('a', 'Colin', 'abcd')
        self.assertEqual('A', user.roll)
        user = UserClass('Admin', 'Colin', 'abcd')
        self.assertEqual('A', user.roll)
        with self.assertRaises(ValueError, msg="Roll must be an admin, professor, or TA"):
            user = UserClass('B', 'Colin', 'abcd')
            user = UserClass('', 'Colin', 'abcd')
            user = UserClass(1, 'Colin', 'abcd')

    def test_Name(self):
        user = UserClass('A','COLIN','abcd')
        self.assertEqual('COLIN', user.name)
        user = UserClass('A', 'colin', 'abcd')
        self.assertEqual('COLIN', user.name)
        user = UserClass('A', 'CoLiN', 'abcd')
        self.assertEqual('COLIN', user.name)
        user = UserClass('A',1234,'abc')
        self.assertEqual('1234', user.name)

    def test_password(self):
        user = UserClass('A', 'Colin', 'abcd')
        self.assertEqual('abcd', user.password)
        user = UserClass('A', 'Colin', 'AbCd')
        self.assertNotEqual('ABCD', user.Password)
        self.assertNotEqual('ABCD', user.getPassword())
        user = UserClass('A', 'Colin', 1234)
        self.assertEqual('1234',user.password)
        self.assertEqual('1234',user.getPassword())

    def test_AddUser(self):
        user = UserClass('A','John','Test')
        self.assertEqual(True, user.addUser())
        user = UserClass('A', 'John', 'Test')
        self.assertEqual(False, user.addUser())
        user = UserClass('A', 'Susan', 'Test')
        self.assertEqual(True, user.addUser())

    def test_RemoveUser(self):
        pass