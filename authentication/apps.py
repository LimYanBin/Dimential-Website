from django.apps import AppConfig


class AuthenticationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'authentication'

class UserConfig(AppConfig):
    name = 'users'
    def ready(self):
        import authentication.signals
