from django.contrib.auth.backends import ModelBackend
from main.models import User


class AccountBackend(ModelBackend):
    def authenticate(self, request, login=None, password=None, **kwargs):
        try:
            account = User.objects.get(email=login)
        except User.DoesNotExist:
            return None

        if account.check_password(password):
            return account

    def get_user(self, user_id):
        try:
            return User.objects.get(user_id=user_id)
        except User.DoesNotExist:
            return None
