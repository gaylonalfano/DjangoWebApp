from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    # After creating SIGNALS to automatically create a user profile each time a new user
    # is created and automatically save the profile each time the User object gets saved,
    # need to import our signals inside of the ready function of our apps.py module.
    def ready(self):
        import users.signals
