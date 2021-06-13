from django.contrib import admin

# Register your models here.
from .models import Animal
from .models import Weight
from .models import Sex

admin.site.register(Animal)
admin.site.register(Weight)
admin.site.register(Sex)
