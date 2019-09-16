from django.db import models
STATUS_CHOICES = [
    ('new', 'Новая'),
    ('in_progress', 'В процессе'),
    ('done', 'Сделано')]


class Task(models.Model):
    status = models.CharField(max_length=50, null=False, blank=False, verbose_name='Статус',
                              default=STATUS_CHOICES[0][0], choices=STATUS_CHOICES)
    description = models.CharField(max_length=100, null=False, blank=False, verbose_name='Описание')
    full_description = models.TextField(max_length=300, null=True, blank=True, verbose_name='Полное описание')
    execution_date = models.DateField(verbose_name='Дата выполнения', null=True, blank=True, default=None)

    def __str__(self):
        return self.description
