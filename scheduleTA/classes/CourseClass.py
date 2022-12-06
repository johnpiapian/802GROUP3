"""
This class deals with things related Course
"""
from app.models import User, Course, Section

class CourseClass:

    def __int__(self):
        pass

    # given a name check if there exists an account
    # associated with the name in the database
    def courseExists(self, name) -> bool:
        try:
            result_from_database = CourseClass.getCourse(self, name)
        except:
            return False
        if result_from_database is None:
            return False
        return True

    # given a valid name return the associated course
    # note: could also make it %like% instead of =equal=
    def getCourse(self, courseName) -> object:
        try:
            result_from_database = Course.objects.get(name=courseName)
        except:
            return None
        return result_from_database

    def getCourse(self, courseID) -> object:
        try:
            result_from_database = Course.objects.get(id=courseID)
        except:
            return None
        return result_from_database

    # given course object store it in the database
    def addCourse(self, courseObj) -> bool:
        if CourseClass.courseExists(self, courseObj.name):
            return False
        try:
            courseObj.save()
        except:
            return False
        return True

    # given course object update the associated course
    # course object must contain name to find which record to update
    def updateCourse(self, courseObj) -> bool:
        course = CourseClass.getCourse(self, courseObj.name)
        if course != None:
            try:
                courseObj.save()
                return True
            except:
                return False
        return False

    # given a valid name delete the associated course
    def deleteCourse(self, courseName) -> bool:
        removeCourse = CourseClass.getCourse(self, courseName)
        if removeCourse != None:
            try:
                User.objects.filter(name=courseName).delete()
            except:
                return False
            return True
        return False

    def deleteCourse(self, courseID) -> bool:
        removeCourse = CourseClass.getCourse(self, courseID)
        if removeCourse != None:
            try:
                User.objects.filter(id=courseID).delete()
            except:
                return False
            return True
        return False