from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager

# Create your models here.

class CustomUserManager(BaseUserManager):
  def create_user(self, username, email, password, **extra_fields):
    if not email:
      raise ValueError("Please provide an email")
    if not password:
      raise ValueError("Please provide a valid password")

    if not extra_fields.get('is_superuser', False):
      # extra_fields.get('is_superusr', False) checks if it a superuser
      # if no value is given it gives it False. if not False passes the if
      # statement and moves to the nested if statement to check the
      # date of birth and profile photo
      if not extra_fields.get('date_of_birth'):
        raise ValueError(f"Please provide date of birth before proceeding")
      if not extra_fields.get('profile_photo'):
        raise ValueError(f"Please provide a profile photo before proceeding")
    # The above codes enforces the provision of date_of_birth and
    # profile_photo for normal users

    email= self.normalize_email(email)
    # converts email to lowercase
    user = self.model(username=username, email= email, **extra_fields)
    # creates an object called user from the cusromUser model
    user.set_password(password)  
    # ensures that a hashed password is stored
    user.save(using=self._db)
    # saves the object to the right database
    return user
    # return the user object

  def create_superuser(self, username, email, password, **extra_fields):
    extra_fields.setdefault('is_staff', True)
    extra_fields.setdefault('is_superuser', True)

    if extra_fields.get('is_staff') is not True:
      raise ValueError("Superuser must have is_staff=True.")
    if extra_fields.get('is_superuser') is not True:
      raise ValueError("Superuser must have is_superuser=True.")

    return self.create_user(username, email, password, **extra_fields)

class CustomUser(AbstractUser):
  date_of_birth = models.DateField(null = True, blank = True)
  profile_photo = models.ImageField(null = True, blank = True)

  objects = CustomUserManager()
  # links customUserManager to customerUser model. customUserManager manages customerUser.

