from django.db import models

class Animal(models.Model):  
    nickname = models.CharField(max_length=100)
    breed = models.TextField()
    description = models.TextField() 
    arrival_date = models.TimeField(auto_now_add=True)
    
    type_of_animal = models.ForeignKey('Type_of_animal', on_delete=models.CASCADE) # реализовал мерезотдельную модель чтобы можно было добавлять новых в админ-панели
    
    photo = models.ImageField(upload_to='uploads/%Y/%m/%d/', blank=True)
    BOY = 'B'
    GIRL = 'G'
    type_of_gender = [
        (BOY, 'Boy'),
        (GIRL, 'Girl'),
    ]
    gender = models.CharField(
        max_length=1,
        choices=type_of_gender,
        default=BOY,
    )
    availability_of_reference = models.BooleanField(default=False)
    age = models.SmallIntegerField()  

    def __str__(self):
        return self.nickname

class Type_of_animal(models.Model):
    type_name = models.CharField(max_length=100)
    description = models.TextField() 

    def __str__(self):  
        return self.type_name