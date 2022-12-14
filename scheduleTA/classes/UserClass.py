"""
This class deals with things related Account
"""
from django.shortcuts import render, redirect
from django.views import View
from app.models import User, Course, Class


class UserClass:

    def __int__(self):
        pass

    # given a name check if there exists an account
    # associated with the name in the database
    def userExists(self, userName) -> bool:
        # noinspection PyBroadException
        try:
            return UserClass.getUser(self, userName) is not None
        except:
            return False

    def authenticate(self, userName, userPassword):
        # noinspection PyBroadException
        try:
            # for insensitivity
            userName = userName.upper()
            if not UserClass.userExists(self, userName):
                return False
            return User.objects.get(name=userName, password=userPassword).name == userName
        except:
            return False

    def getRole(self, userName):
        # noinspection PyBroadException
        try:
            # for insensitivity
            userName = userName.upper()
            return User.objects.filter(name=userName).values_list('role', flat=True)[0]
        except:
            return None

    def getAllUsers(self) -> list:
        try:
            return User.objects.all()
        except:
            return None

    # given a valid name return the associated account
    # note: should only return non-sensitive information
    def getUser(self, userName) -> object:
        # noinspection PyBroadException
        try:
            # for insensitivity
            userName = userName.upper()
            return User.objects.get(name=userName)
        except:
            return None

    # get user by id
    def getUserByID(self, userID):
        # noinspection PyBroadException
        try:
            return User.objects.get(id=userID)
        except:
            return None

    def getUserClasses(self, userObj):
        try:
            tempObj = Class.objects.filter(teacher_name=userObj).values('course')
            return Class.objects.filter(course__in=tempObj)
        except:
            return None

    # given user object store it in the database
    def addUser(self, userObj) -> bool:
        # noinspection PyBroadException
        try:
            # for insensitivity
            userObj.name = userObj.name.upper()
            if UserClass.userExists(self, userObj.name):
                return False
            userObj.save()
            return True
        except:
            return False

    # TODO: need to revisit
    # given user object update the associated account
    # user object must contain name to find which record to update
    def updateUser(self, userObj) -> bool:
        try:
            user_is_modified = False

            tempUser = User.objects.get(id=userObj.id)
            if tempUser.name != userObj.name.upper():
                tempUser.name = userObj.name.upper()
                user_is_modified = True

            if len(userObj.password) > 0 and tempUser.password != userObj.password:
                tempUser.password = userObj.password
                user_is_modified = True

            if userObj.role is not None and tempUser.role != userObj.role:
                tempUser.role = userObj.role
                user_is_modified = True

            if tempUser.skills != userObj.skills:
                tempUser.skills = userObj.skills
                user_is_modified = True

            if user_is_modified:
                tempUser.save()
                return True
            else:
                return False
        except:
            return False

    # given a valid name delete the associated account
    def deleteUser(self, userName) -> bool:
        try:
            if UserClass.userExists(self, userName):
                User.objects.filter(name=userName).delete()
                return True
            else:
                return False
        except:
            return False

## dont think we actually need these
    def getSkills(self, userName):
        try:
            userName = userName.upper()
            return User.objects.filter(name=userName).values_list('skills', flat=True)[0]
        except:
            return None

    def updateSkills(self, userObj, userSkills):
        try:
            tempUser = User.objects.get(id=userObj.id)
            tempUser.skills = userSkills
            tempUser.save()
            return True
        except:
            return False