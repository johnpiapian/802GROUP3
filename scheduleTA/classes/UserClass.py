"""
This class deals with things related Account
"""
from django.shortcuts import render, redirect
from django.views import View
from app.models import User, Course, Section


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
        if UserClass.userExists(self, userObj.name) and len(userObj.password) > 1 and len(userObj.role) == 1:
            try:
                userObj.save()
                return True
            except:
                return False
        return False

    # given a valid name delete the associated account
    def deleteUser(self, userName) -> bool:
        try:
            # for insensitivity
            userName = userName.upper()
            if UserClass.userExists(userName):
                User.objects.filter(name=userName.upper()).delete()
                return True
            else:
                return False
        except:
            return False
