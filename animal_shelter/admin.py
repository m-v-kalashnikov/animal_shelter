from django.contrib import admin
from animal_shelter.models import Animal, Type_of_animal


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    pass

@admin.register(Type_of_animal)
class Type_of_animallAdmin(admin.ModelAdmin):
    pass