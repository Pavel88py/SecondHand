import datetime
from django.db import models
from django.contrib.auth.models import User


class Item(models.Model):
    author = models.ForeignKey(User, verbose_name='Автор')
    name = models.CharField(verbose_name='название', max_length=32)
    category = models.ForeignKey('Category', verbose_name='категория')
    image = models.ImageField(upload_to='', blank=True)
    # Видео будет добавляться в качестве ссылки на сторонний ресурс
    video = models.URLField(blank=True)
    rating = models.PositiveIntegerField(verbose_name='рейтинг', default=0)
    description = models.TextField(verbose_name='описание', blank=True)


class Comment(models.Model):
    author = models.ForeignKey(User, verbose_name='Автор')
    body = models.TextField()
    timestamp = models.DateTimeField(default=datetime.datetime.now)
    item = models.ForeignKey('Item')

    class Meta:
        ordering = ("-timestamp",)


class Category(models.Model):
    name = models.CharField(verbose_name=u'название', max_length=16)
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return self.name
