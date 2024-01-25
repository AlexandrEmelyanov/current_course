from django.db import models


class CurrencyRate(models.Model):
    created = models.DateTimeField(verbose_name='Creation date', auto_now_add=True)
    course = models.FloatField(verbose_name='Course')
    last_update = models.DateTimeField(verbose_name='Last update')

    def __str__(self):
        return f'Currency rate #{self.id}, value: {self.course} RUB'

    class Meta:
        verbose_name = 'Currency rate'
        verbose_name_plural = 'Currency rates'
