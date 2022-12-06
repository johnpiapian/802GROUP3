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
        result_from_database = None
        # noinspection PyBroadException
        try:
            result_from_database = UserClass.getUser(self, userName.upper())
        except:
            return False
        if result_from_database is None:
            return False
        return True

    def passwordCorrect(self, userObject, password):
        try:
            return userObject.password == str(password)
        except:
            return False

    # given a valid name return the associated account
    # note: should only return non-sensitive information
    def getUser(self, userName) -> object:
        result_from_database = None
        # noinspection PyBroadException
        try:
            result_from_database = User.objects.get(name=userName.upper())
        except:
            return None
        return result_from_database

    # given user object store it in the database
    def addUser(self, userObj) -> bool:
        if UserClass.userExists(self,userObj.name):
            return False
        try:
            userObj.save()
        except:
            return False
        return True

    # given user object update the associated account
    # user object must contain name to find which record to update
    def updateUser(self, userObj) -> bool:

        if UserClass.userExists(self,userObj.name) and len(userObj.password)>1 and len(userObj.role) == 1:
            try:
                userObj.save()
                return True
            except:
                return False
        return False

    # given a valid name delete the associated account
    def deleteUser(self, userName) -> bool:

        removeUser = UserClass.getUser(self, userName)
        if removeUser!= None:
            try:
                User.objects.filter(name=userName.upper()).delete()
            except:
                return False
            return True
        return False