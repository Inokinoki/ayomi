from django.contrib.auth.models import User

"""
In fact, we should not put DAO in model, 
I prefered to put it in a file like utils.py or something else.
But just let it go.
"""


class UserDataAccessException(Exception):
    def __init__(self, reason):
        self._reason = reason

    def __str__(self):
        return str(self._reason)


class UserDataAccessObject(object):
    """
    Data Access Object for auth User model
    """

    def __new__(cls, user):
        if isinstance(user, User):
            return super(UserDataAccessObject, cls).__new__(cls)
        else:
            return None

    def __init__(self, user):
        self._user = user

    def get_username(self):
        if self._user:
            return self._user.username
        else:
            raise UserDataAccessException("No user object")

    def set_email(self, email):
        if self._user:
            self._user.email = email
        else:
            raise UserDataAccessException("No user object")

    def get_email(self):
        if self._user:
            return self._user.email
        else:
            raise UserDataAccessException("No user object")

    def set_first_name(self, first_name):
        if self._user:
            self._user.first_name = first_name
        else:
            raise UserDataAccessException("No user object")

    def get_first_name(self):
        if self._user:
            return self._user.first_name
        else:
            raise UserDataAccessException("No user object")

    def set_last_name(self, last_name):
        if self._user:
            self._user.last_name = last_name
        else:
            raise UserDataAccessException("No user object")

    def get_last_name(self):
        if self._user:
            return self._user.last_name
        else:
            raise UserDataAccessException("No user object")

    def save(self):
        if self._user:
            self._user.save()
        else:
            raise UserDataAccessException("No user object")

    def __dict__(self):
        if self._user:
            return {
                "email": self._user.email,
                "first_name": self._user.first_name,
                "last_name": self._user.last_name,
                "username": self._user.username,
            }
        else:
            return {
                "email": "",
                "first_name": "",
                "last_name": "",
                "username": ""
            }

# We do not need to create other model
