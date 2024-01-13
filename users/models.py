from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.db import models


class User(AbstractUser):
    """
    Main User model
    """

    USERNAME_FIELD = "phone"

    GENDER_CHOICE = [
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Others"),
    ]

    # Basic entries
    updated_at = models.DateTimeField(auto_now=True)
    
    first_name = None
    last_name = None
    username = None  # disable the existing username function
    
    name = models.CharField(max_length=120, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICE, null=True)
    phone = models.CharField(max_length=15, unique=True)
    email = models.CharField(max_length=254, null=True)
    dob = models.DateField(null=True)
    avatar = models.CharField(max_length=250, null=True)

    # security related entries
    is_superuser = models.BooleanField(
        default=False,
        help_text="Designates that this user has all permissions without explicitly assigning them.",
        verbose_name="superuser status",
    )
    is_staff = models.BooleanField(
        default=False,
        help_text="Designates whether the user can log into this admin site.",
        verbose_name="staff status",
    )
    is_active = models.BooleanField(
        default=True,
        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
        verbose_name="active",
    )

    def get_full_name(self):
        # The user's Name
        return self.name

    def get_username(self):
        # The user's username
        return self.phone

    def get_short_name(self):
        # The user's first name
        return self.name

    def get_id(self):
        # The user's row id
        return self.id

    def __str__(self):  # __unicode__ on Python 2
        return self.phone

    def has_perm(self, perm, obj=None):
        # "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        # "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def active(self):
        # "Is the user active?"
        return self.is_active
