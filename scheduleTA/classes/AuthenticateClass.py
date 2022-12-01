"""
This class deals with things related to authentication
"""


class AuthenticateClass:
    # return true if successful or false if not
    # this will also set session if login was successful
    def login(self, name, password) -> bool:
        pass

    # upon calling this method use should be logged out
    def logout(self) -> bool:
        pass
