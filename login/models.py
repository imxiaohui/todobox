from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, PermissionsMixin

class TodoUser(models.Model):
	user = models.OneToOneField(User)
	if_registered = models.BooleanField(default=True)

