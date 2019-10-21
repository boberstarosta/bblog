from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        """Import signals to hook up Profile to User."""
        import users.signals
