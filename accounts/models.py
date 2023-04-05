from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    address = models.CharField(max_length=150, blank=True, verbose_name='Endereço')
    is_student = models.BooleanField(default=False, verbose_name='Aluno')
    is_teacher = models.BooleanField(default=False, verbose_name='Professor')
    user_image = models.ImageField(upload_to="user_images/%Y/%m/%d/", blank=True)
