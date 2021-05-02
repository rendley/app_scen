from django.db import models


class Title(models.Model):
    """Класс заголовка страницы"""
    header = models.CharField(verbose_name='Заголовок', max_length=1000)

    def __str__(self):
        return self.header


class Implementation(models.Model):
    """Класс способов реализации угроз"""
    name = models.CharField(verbose_name='Способ реализации', max_length=1000)
    image = models.ImageField(verbose_name='Изображение', blank=True)

    def __str__(self):
        return self.name


class Tactics(models.Model):
    """Класс Тактик"""
    name = models.CharField(verbose_name='Название тактики', max_length=1000)
    slug = models.SlugField(unique=True)
    description = models.TextField(verbose_name='Описание тактики', null=True)
    # number_unique = models.PositiveIntegerField(verbose_name='Идентификатор тактики')

    def __str__(self):
        return self.name


class Technics(models.Model):
    """Класс Техник"""
    tactics = models.ForeignKey(Tactics,
                                verbose_name='Тактика',
                                on_delete=models.CASCADE,
                                related_name='technics')

    name = models.CharField(verbose_name='Название техники', max_length=1000)
    slug = models.SlugField(unique=True)
    number = models.FloatField(verbose_name='Номер техники')
    description = models.TextField(verbose_name='Описание техники', null=True)

    def __str__(self):
        return self.name






