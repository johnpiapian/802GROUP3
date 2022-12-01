from django.test import TestCase
from app.models import User

class LoginUnitTests(TestCase):

    def setUp(self):
        self.Admin = User.objects.create(role='A', name='Admin1!', password='Password')
        self.Colin = User.objects.create(role='A',name='Colin',password='1234')
        self.George = User.objects.create(role='T', name='George', password="1234")
        self.Humraj = User.objects.create(role='T',name='Humraj', password='pAsSwOrD')
        self.Nicholas = User.objects.create(role='P',name='Nicholas',password='a!2/}')
        self.Sut = User.objects.create(role='P',name='Sut',password='abcd')

        self.userList = User.objects.all()

    def badName(self):
        pass

    def badPassword(self):
        pass

    def noName(self):
        pass

    def noPassword(self):
        pass

    def wrongPassword(self):
        pass

    def noSuchUser(self):
        pass

    def goodLogin(self):
        pass