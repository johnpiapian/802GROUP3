"""
This class deals with things related Class
"""
from app.models import Class


class ClassClass:

    def __int__(self):
        pass

    # given a course and class number check if there exists an account
    # associated with the class name in the database
    def classExists(self, classNumber, course) -> bool:
        try:
            result_from_database = ClassClass.getClass(self, classNumber, course)
        except:
            return False
        if result_from_database is None:
            return False
        return True

    def getAllClasses(self):
        try:
            return Class.objects.all()
        except:
            return None

    # given a course and classNumber return the associated class
    def getClass(self, classNumber,course) -> object:
        try:
            result_from_database = Class.objects.get(class_number=classNumber, course=course)
        except:
            return None
        return result_from_database

    # given class object store it in the database
    def addClass(self, classObj) -> bool:
        try:
            if ClassClass.classExists(self, classObj.class_number,classObj.course):
                return False
            classObj.save()
            return True
        except:
            return False

    # given class object update the associated class
    # class object must contain name to find which record to update
    def updateClass(self, classObj) -> bool:
        c = ClassClass.getClass(self, classObj.class_number)
        if c != None:
            try:
                classObj.save()
                return True
            except:
                return False
        return False

    def deleteClass(self, classNumber,course) -> bool:
        try:
            Class.objects.filter(class_name=classNumber,course=course).delete()
            return True
        except:
            return False
