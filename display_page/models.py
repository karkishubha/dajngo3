from django.db import models

from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
def __str__(self):
    return 'f{self.first_name} {self.last_name}'
class musician (models.Model):
    first_name = models.CharField(max_length=30, verbose_name="Full name")
    age = models.PositiveBigIntegerField(help_text= 'Enter age')
    instrument = models.CharField(max_length=30)

    class Meta:
        db_table = 'musician'