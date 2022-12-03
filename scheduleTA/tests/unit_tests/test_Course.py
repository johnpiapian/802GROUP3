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

    def test_getCourse_00(self):
        for i in self.courseList:
            self.assertEqual(i, CourseClass.CourseClass.getCourse(self,i.name))
            self.assertEqual(i, CourseClass.CourseClass.getCourse(self,i.id.__str__))
            self.assertEqual(i, CourseClass.CourseClass.getCourse(self,i.id))
    def test_getCourse_01(self):
        self.assertEqual(None, CourseClass.CourseClass.getCourse(self,''))
    def test_addCourse_00(self):
        self.assertEqual(True,CourseClass.CourseClass.addCourse(self,['Art','4']))
    def test_addCourse_01(self):
        self.assertEqual(False,CourseClass.CourseClass.addCourse(self,['Art','4']))
    def test_addCourse_02(self):
        self.assertEqual(False,CourseClass.CourseClass.addCourse(self,['Art','2']))
    def test_addCourse_03(self):
        self.assertEqual(True,CourseClass.CourseClass.addCourse(self,['Music',4]))
    def test_addCourse_04(self):
        self.assertEqual(False,CourseClass.CourseClass.addCourse(self,['Gym','']))


    def test_updateCourse_00(self):
        self.assertEqual(True, CourseClass.CourseClass.updateCourse(self,['Math','3']))
    def test_updateCourse_01(self):
        self.assertEqual(False, CourseClass.CourseClass.updateCourse(self,['Math', '3']))
    def test_updateCourse_02(self):
        self.assertEqual(False, CourseClass.CourseClass.updateCourse(self,['', '3']))
    def test_updateCourse_03(self):
        self.assertEqual(False, CourseClass.CourseClass.updateCourse(self,['JDJDJ', '3']))
    def test_updateCourse_04(self):
        self.assertEqual(False, CourseClass.CourseClass.updateCourse(self,['English', '']))
    def test_updateCourse_05(self):
        self.assertEqual(True, CourseClass.CourseClass.updateCourse(self,['English', 1]))

    def test_deleteCourse_00(self):
        self.assertEqual(True,self.courseList.contains(self.Math))
    def test_deleteCourse_01(self):
        self.assertEqual(True,CourseClass.CourseClass.deleteCourse(self,'Math'))
    def test_deleteCourse_02(self):
        self.assertEqual(False,self.courseList.contains(self.Math))
    def test_deleteCourse_03(self):
        self.assertEqual(False,CourseClass.CourseClass.deleteCourse(self,'Math'))
    def test_deleteCourse_04(self):
        self.assertEqual(False,CourseClass.CourseClass.deleteCourse(self,''))
    def test_deleteCourse_05(self):
        self.assertEqual(False, CourseClass.CourseClass.deleteCourse(self,'Gym'))
    def test_deleteCourse_06(self):
        self.assertEqual(False, CourseClass.CourseClass.deleteCourse(self,3))

