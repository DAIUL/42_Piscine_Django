from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin, Group, Permission

class UserInfosManager(BaseUserManager):
	def create_user(self, username, password, **extra_fields):
		if not username:
			raise ValueError("Users must have a username")
		user = self.model(username=username, **extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, username, password=None, **extra_fields):
		extra_fields.setdefault("is_staff", True)
		extra_fields.setdefault("is_superuser", True)
		return self.create_user(username, password, **extra_fields)

class UserInfos(AbstractBaseUser, PermissionsMixin):
	username = models.CharField(max_length=32, unique=True)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)

	objects = UserInfosManager()

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = []