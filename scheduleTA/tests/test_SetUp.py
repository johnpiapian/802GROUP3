from django.test import TestCase, Client
##need to import user models once they are implemented.
from app.models import User, Course, Class

class dbSetup(TestCase):
    # set up database for tests
    mockUser = None
    userList = None
    def setUp(self):
        self.mockUser = Client()
        self.Admin = User.objects.create(role='A', name='ADMIN1!', password='Password')
        self.Colin = User.objects.create(role='A', name='COLIN', password='1234')
        self.George = User.objects.create(role='T', name='GEORGE', password="1234")
        self.Humraj = User.objects.create(role='T', name='HUMRAJ', password='pAsSwOrD')
        self.Nicholas = User.objects.create(role='P', name='NICHOLAS', password='a!2/}')
        self.Sut = User.objects.create(role='P', name='SUT', password='abcd')
        self.Lisa = User(role='A', name='LISA', password='test')
        self.ColinPchange = User(role='A', name = 'COLIN', password='Test')
        self.ColinRchange = User(role='P', name='COLIN', password='1234')


        self.userList = User.objects.all()

        self.Math = Course.objects.create(id=666,name='MATH',credit=4)
        self.Sci = Course.objects.create(name='SCIENCE',credit=3)
        self.eng = Course.objects.create(id=555,name='ENGLISH',credit=4)

        self.MathChange = Course(id=666,name='MATH',credit=2)
        self.engChange = Course(id=555, name='', credit=4)

        self.art = Course(name="ART",credit=4)
        self.music= Course(name='MUSIC',credit=2)
        self.Gym = Course(name='GYM',credit=1)

        self.courseList = Course.objects.all()




