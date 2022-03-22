from django.db import models


class User(models.Model):
    name        = models.CharField(max_length=70)
    last_name   = models.CharField(max_length=70)
    user_name   = models.CharField(max_length=70)
    email       = models.EmailField(max_length=256)
    address     = models.CharField(max_length=70)
    remmeber_me = models.BooleanField()

    def __str__(self) -> str:
        return f"{self.name} {self.last_name}"