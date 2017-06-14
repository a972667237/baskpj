#coding: utf-8
from django.db import models
from DjangoUeditor.models import UEditorField
# Create your models here.

class StarDetail(models.Model):
    name = models.CharField(u'name', max_length=200)
    introduce = UEditorField(u'introduce', max_length=1000)
    class Meta:
        verbose_name = u'star'
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return self.name

class Comment(models.Model):
    article = models.ForeignKey("StarDetail")
    user_email = models.EmailField(max_length=254)
    content = UEditorField(u'content', max_length=200)
    create_time = models.DateField(u'time', auto_now_add=True)
    def __unicode__(self):
        return self.content[0:3] + '>>>'
    class Meta:
        verbose_name = u'comment'
        verbose_name_plural = verbose_name
