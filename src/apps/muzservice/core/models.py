from django.db import models


class TimestampedModel(models.Model):
    """ Модель временных отметок """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created_at', '-updated_at']


class ActivityMarkModel(models.Model):
    """ Модель флага активных элементов """
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True