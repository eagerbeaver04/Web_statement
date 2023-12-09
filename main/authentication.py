from django.contrib.auth.backends import ModelBackend
from main.models import Account


class AccountBackend(ModelBackend):
    def authenticate(self, request, login=None, password=None, **kwargs):
        try:
            account = Account.objects.get(login=login)
        except Account.DoesNotExist:
            return None

        if account.check_password(password):
            return account.user


    def get_user(self, user_id):
        try:
            return Account.objects.get(user_id=user_id).user
        except Account.DoesNotExist:
            return None
