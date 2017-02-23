from __future__ import unicode_literals
import re, bcrypt

from django.db import models

EMAIL_REGEX = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

#Password reqs: 8 chars min, 1 upper, 1 lower, 1 number
PASSWORD_REGEX = r"(^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$)"

class UserManager(models.Manager):
    def register(self, data):
        errors = []
        if len(data['first_name']) < 2:
            errors.append('First name must be at least 1 character')

        if len(data['last_name']) < 2:
            errors.append('Last name must be at least 1 character')

        if any (char.isdigit() for char in data['first_name']):
            errors.append("First name can't contain integers")

        if any (char.isdigit() for char in data['last_name']):
            errors.append("Last name can't contain integers")

        if not re.match(EMAIL_REGEX, data['email']):
            errors.append('Please input a valid email address')

        user = User.objects.filter(email=data['email'])

        if user:
            errors.append('User already exists')

        if not re.match(PASSWORD_REGEX, data['password']):
            errors.append('Password not valid, reqs are: 8 characters minimum, 1 upper, 1 lower, and 1 number')

        if data['password'] != data['confirm_pw']:
            errors.append("Password and Confirm pw don't match")


        if errors:
            return (False, errors)

        else:
            new_user = User.objects.create(
                firstname = data['first_name'],
                lastname = data['last_name'],
                email = data['email'],
                password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt()),
            )
            return (True, new_user)

    def login(self, data):
        errors = []

        if not re.match(EMAIL_REGEX, data['email']):
            errors.append('Please input a valid email address')

        try:
            user = User.objects.get(email=data['email'])
            print ">>>>>>>>user is----->>>>>>>", user

            print ">>>>>>>password is-------->>>>>>>", user.password
        except NameError:
            errors.append("Username/Password combo is invalid")
            print "errors are------->>>>>>>>", errors


        if bcrypt.hashpw(data['password'].encode('utf-8'), user.password.encode('utf-8')) != user.password:
            errors.append("Username/Password combo is invalid")

        if errors:
            return (False, errors)

        else:
            return (True, user)


class User(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    def __str__(self):
        return self.firstname
