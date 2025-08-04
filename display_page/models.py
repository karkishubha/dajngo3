from django.db import models

from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
class musician (models.Model):
    first_name = models.CharField(max_length=30, verbose_name="Full name")
    age = models.PositiveBigIntegerField(help_text= 'Enter age')
    instrument = models.CharField(max_length=30)

    class Meta:
        db_table = 'musician'
Districts = [
    ("ktm", "kathmandu"),
    ("Bkt", "Bhaktapur"),
    ("Llp", "Lalitpur"),
    ("Phk", "Pokhara"),
    
]
class citizenship (models.Model):
    citizenship_number=models.PositiveIntegerField(max_length=30,primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    issued_date=models.DateField()
    issued_date_my=models.DateField(auto_now_add=True)
    district = models.CharField(max_length=30, choices=Districts)
    person = models.OneToOneField(Person,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.citizenship_number}"
class Car (models.Model):
    
    car_name = models.CharField(max_length=30)
    
    person = models.ForeignKey(Person,on_delete=models.CASCADE)

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    

    def __str__(self):
        return f"{self.name}"
class Articles(models.Model):
    title=models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)