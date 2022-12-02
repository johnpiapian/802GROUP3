from classes import CourseClass
from tests import test_SetUp
class CourseUnitTest(test_SetUp.dbSetup):

    def setUp(self):
        super().setUp()

    def test_courseExists(self):
        for i in self.courseList:
            self.assertEqual(True,CourseClass.courseExists(i.name))
        self.assertEqual(False, CourseClass.courseExists(''))
        self.assertEqual(False, CourseClass.courseExists('4'))
        self.assertEqual(False, CourseClass.courseExists(4))

    def test_getCourse(self):
        for i in self.courseList:
            self.assertEqual(i, CourseClass.getCourse(i.name))
            self.assertEqual(i, CourseClass.getCourse(i.id.__str__))
            self.assertEqual(i, CourseClass.getCourse(i.id))
        self.assertEqual(None, CourseClass.getCourse(''))
    def test_addCourse(self):
        self.assertEqual(True,CourseClass.addCourse(['Art','4']))
        self.assertEqual(False,CourseClass.addCourse(['Art','4']))
        self.assertEqual(False,CourseClass.addCourse(['Art','2']))
        self.assertEqual(True,CourseClass.addCourse(['Music',4]))
        self.assertEqual(False,CourseClass.addCourse(['Gym','']))


    def test_updateCourse(self):
        self.assertEqual(True, CourseClass.updateCourse(['Math','3']))
        self.assertEqual(False, CourseClass.updateCourse(['Math', '3']))
        self.assertEqual(False, CourseClass.updateCourse(['', '3']))
        self.assertEqual(False, CourseClass.updateCourse(['JDJDJ', '3']))
        self.assertEqual(False, CourseClass.updateCourse(['English', '']))
        self.assertEqual(True, CourseClass.updateCourse(['English', 1]))

    def test_deleteCourse(self):
        self.assertContains(self.courseList, self.Math)
        self.assertEqual(True,CourseClass.deleteCourse('Math'))
        self.assertNotContais(self.courseList,self.Math)
        self.assertEqual(False,CourseClass.deleteCourse('Math'))
        self.assertEqual(False,CourseClass.deleteCourse(''))
        self.assertEqual(False, CourseClass.deleteCourse('Gym'))
        self.assertEqual(False, CourseClass.deleteCourse(3))

