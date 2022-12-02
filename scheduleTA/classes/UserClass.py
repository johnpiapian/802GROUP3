"""
This class deals with things related Account
"""


class UserClass:

    def __int__(self):
        pass

    # given a name check if there exists an account
    # associated with the name in the database
    def userExists(self, userName) -> bool:
        pass

    # given a valid name return the associated account
    # note: should only return non-sensitive information
    def getUser(self, userName) -> object:
        pass

    # given user object store it in the database
    def addUser(self, userObj) -> bool:
        pass

    # given user object update the associated account
    # user object must contain name to find which record to update
    def updateUser(self, userObj) -> bool:
        pass

    # given a valid name delete the associated account
    def deleteUser(self, userName) -> bool:
        pass
