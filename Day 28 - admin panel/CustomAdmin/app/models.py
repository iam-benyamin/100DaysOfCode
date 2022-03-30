from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=3)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self) -> str:
        return f'Author: {self.name}'
