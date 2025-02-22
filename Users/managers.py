from django.utils.translation import gettext_lazy as q
from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(q('The Email must be set'))

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_staff(self, email, **extra_fields):
        """
        Create and save a User with the given email as a staff.
        """

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)

        if not email:
            raise ValueError(q('The Email must be set'))

        if extra_fields.get('is_staff') is not True:
            raise ValueError(q('Superuser must have is_staff=True.'))

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('account_type', "Admin")

        if extra_fields.get('is_staff') is not True:
            raise ValueError(q('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(q('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)
