from django.db import models

# Create your models here.
STATUS_CHOICES = [('new', 'Новая'), ('in_progress', 'В процессе'),  ('done', 'Сделано')]

class Task(models.Model):
    title = models.CharField(max_length=300, null=False, blank=False, verbose_name='title', default='no task name')
    description = models.CharField(max_length=300, null=False, blank=False, verbose_name='description')
    status = models.CharField(max_length=20, null=False, blank=False, choices=STATUS_CHOICES, verbose_name='Status', default=STATUS_CHOICES[0][0])
    deadline = models.DateField(max_length=40, default='', verbose_name='deadline')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')

    def __str__(self):
        return f"{self.id}. {self.description}: {self.status}, {self.deadline}"
