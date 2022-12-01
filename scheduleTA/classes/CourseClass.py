"""
This class deals with things related Course
"""


class CourseClass:
    # given a name check if there exists an account
    # associated with the name in the database
    def courseExists(self, name) -> bool:
        pass

    # given a valid name return the associated course
    # note: could also make it %like% instead of =equal=
    def getCourse(self, name) -> object:
        pass

    def getCourse(self, courseID) -> object:
        pass

    # given course object store it in the database
    def addCourse(self, courseObj) -> bool:
        pass

    # given course object update the associated course
    # course object must contain name to find which record to update
    def updateCourse(self, user) -> bool:
        pass

    # given a valid name delete the associated course
    def deleteCourse(self, name) -> bool:
        pass
