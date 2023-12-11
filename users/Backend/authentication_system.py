from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.db import transaction as trx
from django.forms import model_to_dict

from base.Backend.services import SpinSchoolUsersService


class RegisterUser(object):
    @staticmethod
    def register_user(**kwargs):
        sid = trx.savepoint()
        try:
            username = kwargs.get('username').strip()
            if not username:
                return {"code": "777.777.777", 'message': 'Please provide username!'}
            first_name = kwargs.get('first_name')
            if not first_name:
                return {"code": "777.777.777", 'message': 'Please provide first_name!'}
            last_name = kwargs.get('last_name')
            if not last_name:
                return {"code": "777.777.777", 'message': 'Please provide last_name!'}
            email = kwargs.get('email')
            if not email:
                return {"code": "777.777.777", 'message': 'Please provide email!'}
            password = kwargs.get('password')
            if not password:
                return {"code": "777.777.777", 'message': 'Please provide password!'}
            contacts = kwargs.get('mobile')
            if not contacts:
                return {"code": "777.777.777", 'message': 'Please provide mobile!'}
            gender = kwargs.get('gender')
            print("username", username, "firstname", first_name, "lastname", last_name, "email", email, "password",
                  password)
            user = SpinSchoolUsersService().filter(username=username)
            if user:
                return {"code": '777.777.777', "message": "username already exists"}
            if SpinSchoolUsersService().filter(email=email):
                return {"code": '777.777.777', "message": "email already exists"}
            created_user = SpinSchoolUsersService().create(
                first_name=first_name, username=username, last_name=last_name, email=email, mobile=contacts,
                gender=gender, password=make_password(password))
            return {"code": "100.000.000", "message": "Successful registration", "data": model_to_dict(created_user)}
        except Exception as ex:
            trx.savepoint_rollback(sid)
            print("Error during user registration", ex)
            return {"code": '777.777.777', "message": "Failed"}

    @staticmethod
    def update_user(**kwargs):
        try:
            user_id = kwargs.get('user_id')
            username = kwargs.get('username')
            first_name = kwargs.get('first_name')
            last_name = kwargs.get('last_name')
            gender = kwargs.get('gender')
            email = kwargs.get('email')
            mobile = kwargs.get('mobile')
            if not user_id:
                return {"code": "100.000.021", 'message': 'Please provide user ID!'}
            my_user = SpinSchoolUsersService().get(id=user_id)
            if not my_user:
                return {"code": "100.000.021", 'message': 'user not found!'}
            if not username:
                username = my_user.username
            if not first_name:
                first_name = my_user.first_name
            if not last_name:
                last_name = my_user.last_name
            if not mobile:
                mobile = my_user.mobile
            if not email:
                email = my_user.email
            if not gender:
                gender = my_user.gender
            print(first_name)
            user = SpinSchoolUsersService().get(id=my_user.id)
            if user:
                SpinSchoolUsersService().update(pk=user.id, first_name=first_name, username=username,
                                                last_name=last_name, gender=gender, email=email, mobile=mobile)
            return SpinSchoolUsersService
        except Exception as ex:
            print("Error during user registration", ex)
        return {"code": '100.000.021', "message": "Failed"}

    @staticmethod
    def login_user(request, **kwargs):
        try:
            username = kwargs.get('username')
            password = kwargs.get('password')

            if not username:
                return {"code": "100.000.011", 'message': 'Please provide username!'}
            if not password:
                return {"code": "100.000.011", 'message': 'Please provide password!'}
            user = authenticate(username=username, password=password)
            if not user:
                return {"code": "100.000.011", 'message': 'invalid credentials!'}
            if user.check_password(password):
                login(request, user)
            return {"code": "100.000.000", 'message': 'login successful!'}
        except Exception as ex:
            print("Error during user registration", ex)
        return {"code": '100.000.011', "message": "Failed"}

    @staticmethod
    def logout_user(request, **kwargs):
        username = kwargs.get('username')
        if not username:
            return {"code": "100.000.011", 'message': 'Please provide username!'}
        try:
            if not request.user.is_authenticated:
                logout(request)
            return {"code": "100.000.000", 'message': 'logout successful!'}
        except Exception as ex:
            print("Error during user logout", ex)
            return {"code": '100.000.011', "message": "Failed"}

