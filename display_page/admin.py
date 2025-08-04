from django.contrib import admin
from display_page.models import Person
from display_page.models import musician
from display_page.models import citizenship
from display_page.models import Car
from display_page.models import Author

# Register your models here.
admin.site.register(Person)
admin.site.register(musician)
admin.site.register(citizenship)
admin.site.register(Car)
admin.site.register(Author)

