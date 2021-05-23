from django.db import models

# Create your models here.
<<<<<<< HEAD

class Book(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=300)
    price = models.IntegerField()
    review = models.CharField(max_length=500)

    def __str__(self):
        return self.name


    
=======
class Book (models.Model):
    def __str__(self):
        return self.name
      
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    desc = models.CharField(max_length=300)
    reviews = models.CharField(max_length=500)

>>>>>>> 65f4bf3 (This is my first Django project)
