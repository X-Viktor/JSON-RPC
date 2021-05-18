from django.contrib.auth.models import User
from modernrpc.auth.basic import http_basic_auth_login_required
from modernrpc.core import rpc_method


@rpc_method
def register_user(username, password):
    """Регистрация нового пользователя."""
    try:
        user = User.objects.create_user(username, 'nsg@it.lp', password)
        user.save()
        return 'Регистрация прошла успешно.'
    except:
        return 'Ошибка регистрации.'


@rpc_method
@http_basic_auth_login_required
def change_password(new_password, **kwargs):
    """Изменение пароля авторизованного пользователя."""
    try:
        user = kwargs['request'].user
        user.set_password(new_password)
        user.save()
        return 'Ваш пароль был успешно изменен.'
    except:
        return 'Ошибка смены пароля.'
