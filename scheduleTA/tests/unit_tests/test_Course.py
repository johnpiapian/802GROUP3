from classes import CourseClass
from tests import test_SetUp
class CourseUnitTest(test_SetUp.dbSetup):

    def setUp(self):
        super().setUp()

    def test_courseExists_00(self):
        for i in self.courseList:
            self.assertEqual(True,CourseClass.CourseClass.courseExists(self,i.name))
    def test_courseExists_01(self):
        self.assertEqual(False, CourseClass.CourseClass.courseExists(self,''))
    def test_courseExists_02(self):
        self.assertEqual(False, CourseClass.CourseClass.courseExists(self,'4'))
    def test_courseExists_03(self):
        self.assertEqual(False, CourseClass.CourseClass.courseExists(self,4))

    def test_getCourse_01(self):
        self.assertEqual(None, CourseClass.CourseClass.getCourse(self,''))
    def test_addCourse_00(self):
        self.assertEqual(True,CourseClass.CourseClass.addCourse(self,self.art))
    def test_addCourse_01(self):
        self.assertEqual(False,CourseClass.CourseClass.addCourse(self,self.Math))
    def test_addCourse_02(self):
        self.Math.credit = 2
        self.assertEqual(False,CourseClass.CourseClass.addCourse(self,self.Math))
    def test_addCourse_03(self):
        self.assertEqual(True,CourseClass.CourseClass.addCourse(self,self.music))
    def test_addCourse_04(self):
        self.Gym.credit = ''
        self.assertEqual(False,CourseClass.CourseClass.addCourse(self,self.Gym))

    def test_updateCourse_00(self):
        self.assertEqual(True, CourseClass.CourseClass.updateCourse(self,self.MathChange))
    def test_updateCourse_02(self):
        self.assertEqual(False, CourseClass.CourseClass.updateCourse(self,self.engChange))
    def test_updateCourse_03(self):
        self.assertEqual(False, CourseClass.CourseClass.updateCourse(self,self.Gym))
    def test_updateCourse_04(self):
        self.eng.credit = ''
        self.assertEqual(False, CourseClass.CourseClass.updateCourse(self,self.eng))
    def test_updateCourse_05(self):
        self.eng.credit=1
        self.assertEqual(True, CourseClass.CourseClass.updateCourse(self,self.eng))

    ## every test_ function recreates every mock object.
    ## you CANNOT call .contains in a separate test_ function
    ## because the mock objects are recreated fresh for every test.
    ## -Nick
    ## also, one of tests provided the literal '3' as an argument,
    ## 3 is actually the ID of some mock object so it was deleting it

    def test_deleteCourse_00(self):
        self.assertEqual(True,self.courseList.contains(self.Math))
    def test_deleteCourse_01(self):
        self.assertEqual(True, self.courseList.contains(self.Math))
        self.assertEqual(True,CourseClass.CourseClass.deleteCourse(self,self.Math.id))
        self.assertEqual(False, self.courseList.contains(self.Math))
    def test_deleteCourse_02(self):
        self.assertEqual(True, self.courseList.contains(self.Sci))
        self.assertEqual(True,CourseClass.CourseClass.deleteCourse(self,self.Sci.id))
        self.assertEqual(False, self.courseList.contains(self.Sci))
    def test_deleteCourse_04(self):
        self.assertEqual(False,CourseClass.CourseClass.deleteCourse(self,''))
    def test_deleteCourse_05(self):
        self.assertEqual(False, CourseClass.CourseClass.deleteCourse(self,'Gym'))

