from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
User = settings.AUTH_USER_MODEL
from django_resized import ResizedImageField


class CustomUserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    def _create_user(self, email, password=None, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)



class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

Gender_Choices = (
    ('M', 'Male'),
    ('F', 'Female'),
)
Billing_Choices = (
    ('W', 'Work'),
    ('H', 'Home'),
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1,choices=Gender_Choices, null=True, blank=True)
    mobile = models.CharField(max_length=15, null=True, blank=True)
    image = ResizedImageField(size=[450, 450], quality=75, crop=['middle', 'center'], upload_to='media/user/', null=True, blank=True)
    dob = models.DateField(null=True, blank=True)


class Billing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, default="")
    mobile = models.CharField(max_length=15, default="")
    country = models.CharField(max_length=30, default="")
    state = models.CharField(max_length=30, default="")
    city = models.CharField(max_length=30, default="")
    pin = models.CharField(max_length=6, default="")
    locality = models.CharField(max_length=30, default="")
    address = models.TextField(default="")
    landmark = models.CharField(max_length=30, null=True, blank=True)
    alt_mobile = models.CharField(max_length=15, default="", blank=True)
    type = models.CharField(max_length=2, choices=Billing_Choices, default="M")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name







