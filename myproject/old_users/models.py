from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
import random

class CustomUser(AbstractUser):
    is_active = models.BooleanField(default=False)
    confirmation_code = models.CharField(max_length=6, blank=True, null=True)

    def generate_confirmation_code(self):
        self.confirmation_code = str(random.randint(100000, 999999))
        self.save()

class Confirmation(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    code = models.CharField(max_length=6)
