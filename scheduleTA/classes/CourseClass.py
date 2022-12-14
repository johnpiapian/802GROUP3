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

    def getAllCourses(self):
        try:
            return Course.objects.all()
        except:
            return None

    # given a valid courseID return the associated course
    def getCourse(self, courseID) -> object:
        try:
            result_from_database = Course.objects.get(id=courseID)
        except:
            return None
        return result_from_database

    # given course object store it in the database
    def addCourse(self, courseObj) -> bool:
        try:
            if CourseClass.courseExists(self, courseObj.name):
                return False
            courseObj.save()
            return True
        except:
            return False

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

    def deleteCourse(self, courseID) -> bool:
        try:
            Course.objects.filter(id=courseID).delete()
            return True
        except:
            return False
