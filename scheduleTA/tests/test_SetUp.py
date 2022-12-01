from django.test import TestCase, Client
##need to import user models once they are implemented.
from app.models import User, Course, Section

class dbSetup(TestCase):
    # set up database for tests
    mockUser = None
    userList = None
    def setUp(self):
        self.mockUser = Client()
        self.Admin = User.objects.create(role='A', name='Admin1!', password='Password')
        self.Colin = User.objects.create(role='A', name='Colin', password='1234')
        self.George = User.objects.create(role='T', name='George', password="1234")
        self.Humraj = User.objects.create(role='T', name='Humraj', password='pAsSwOrD')
        self.Nicholas = User.objects.create(role='P', name='Nicholas', password='a!2/}')
        self.Sut = User.objects.create(role='P', name='Sut', password='abcd')

        self.userList = User.objects.all()

        self.Math = Course.objects.create(name='Math',credit='4')
        self.Sci = Course.objects.create(name='Science',credit='3')
        self.eng = Course.objects.create(name='English',creidt='4')

        self.courseList = Course.objects.all()



