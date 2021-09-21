from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    created = models.DateTimeField('Дата создания', auto_now_add=True)
    start_date = models.DateField(
        verbose_name='Дата начала',
        help_text='DD.MM.YYYY'
    )
    start_time = models.TimeField(
        verbose_name='Время начала',
        help_text='HH:MM'
    )
    end_time = models.TimeField(
        blank=True,
        null=True,
        verbose_name='Время окончания',
        help_text='HH:MM',
    )
    responsible = models.CharField(
        max_length=200,
        verbose_name='Ответственный',
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'
        ordering = ['start_date', 'start_time']
        constraints = [
            models.UniqueConstraint(
                fields=['start_date', 'start_time'],
                name='unique_start_date_time'
            )
        ]

    def __str__(self):
        return self.title

    @property
    def all_day(self):
        if self.end_time:
            if (self.end_time.hour - self.start_time.hour) >= 9:
                return True
        return False
