from django.db import models
from django.contrib.auth.models import AbstractUser
from mainapp.models import NULLABLE
# 1:35 6 video

class User(AbstractUser):
    email = models.EmailField(blank=True, verbose_name='Email',
                              unique=False) # временно False - не пускает через вк
    age = models.PositiveSmallIntegerField(verbose_name='Возраст', **NULLABLE)
    avatar = models.ImageField(upload_to='users', verbose_name='Аватарка', **NULLABLE)


    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

