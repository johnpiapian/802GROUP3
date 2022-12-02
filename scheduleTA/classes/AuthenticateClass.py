"""
This class deals with things related to authentication
"""


class Authenticate:

    def __init__(self, name, password):
        self.name = name
        self.password = password

    def validateName(self) -> bool:
        return 0 < len(self.name) < 21

    def validatePassword(self) -> bool:
        return 0 < len(self.password) < 21

    # return true if successful or false if not
    # use the model class to validate if user is valid
    def validateUser(self) -> bool:
        # this is just for testing purposes for now
        if self.name.lower() == "john" and self.password == "123":
            return True
        return False
