from oauth.models.user_device_token import UserDeviceToken
from utils import enums, exceptions, messages
from django.db import models
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from utils.models import AbstractModel

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username=email,
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.active = False
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )

        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )

        user.admin = True
        user.staff = True
        user.active = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, AbstractModel):
    objects = UserManager()

    email = models.EmailField(
        verbose_name='email address',
        max_length=254,
        unique=True,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] # Email & Password are required by default.

    type = models.CharField(max_length=32, choices=enums.UserAccountType.choices, default=enums.UserAccountType.CUSTOMER)

    username = models.CharField(max_length=255, unique=True)

    phone_number = models.CharField(max_length=16, null=True, blank=True)

    first_name = models.CharField(max_length=128, null=True, blank=True)
    last_name = models.CharField(max_length=128, null=True, blank=True)

    description = models.TextField(null=True, blank=True)

    language = models.CharField(default='vietnam', max_length=8)

    admin = models.BooleanField(default=False) # a superuser
    staff = models.BooleanField(default=False) # a admin user; non super-user

    last_login = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    joined_at = models.DateTimeField(auto_now=False, auto_now_add=True)

    active = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        return super(User, self).save(*args, **kwargs)

    def __str__(self):
        return "{} - {}".format(str(self.username), str(self.email))

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    @property
    def is_active(self):
        "Is the user active?"
        return self.active

    @classmethod
    def is_exist(cls, **filter_data):
        return User.objects.filter(**filter_data).exists()

    def generate_access_token(self, **kwargs):
        if not self.is_active:
            raise exceptions.AuthenticationException(messages.INVALID_USER)
        device_token = UserDeviceToken.objects.create(user = self, active=True, **kwargs)
        return device_token