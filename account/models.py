#coding: utf-8
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class BaskUser(models.Model):
    user = models.OneToOneField(User)
    nick = models.CharField('nickname', max_length=100)
    class Meta:
        verbose_name = 'member'
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return self.nick
