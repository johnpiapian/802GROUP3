from classes import ClassClass
from tests import test_SetUp

class ClassUnitTests(test_SetUp.dbSetup):
    def setUp(self):
        super().setUp()

    def test_classExists_00(self):
        for i in self.classList:
            self.assertEqual(True,ClassClass.ClassClass.classExists(self,i.class_number, i.course))
    def test_classExists_01(self):
        self.assertEqual(False, ClassClass.ClassClass.classExists(self,'',''))

    def test_getClass_00(self):
            for i in self.classList:
                self.assertEqual(i, ClassClass.ClassClass.getClass(self,i.class_number,i.course))

    def test_getClass_01(self):
        self.assertEqual(None,ClassClass.ClassClass.getClass(self,'',''))
    def test_addClass_00(self):
            self.assertEqual(True,ClassClass.ClassClass.addClass(self,self.Math107))
    def test_addClass_01(self):
            self.assertEqual(False,ClassClass.ClassClass.addClass(self,self.Math001))
    def test_addClass_01(self):
        self.Math107.course=None
        self.assertEqual(False,ClassClass.ClassClass.addClass(self,self.Math107))

    def test_updateClass_00(self):
        self.assertEqual(True,ClassClass.ClassClass.updateClass(self,self.Math001))

    def test_updateClass_01(self):
        self.assertEqual(False,ClassClass.ClassClass.updateClass(self,self.Math107))

    def test_deleteClass_00(self):
        self.assertEqual(True,ClassClass.ClassClass.deleteClass(self, self.Math001.id))
    def test_deleteClass_01(self):
        self.assertEqual(False,ClassClass.ClassClass.deleteClass(self, ""))