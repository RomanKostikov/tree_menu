from django.db import models


# Create your models here.

class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    url = models.CharField(max_length=255)
    named_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        """
        Возвращает строковое представление объекта.

        :return: Строковое представление объекта.
        :rtype: str
        """
        return self.name
