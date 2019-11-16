from django.db import models

# Create your models here.


class User(models.Model):
    # name = models.CharField(max_length=50)
    height = models.FloatField(default=0.0)
    weight = models.FloatField(default=0.0)
    physique_image = models.ImageField(upload_to='images/')

    def __str__(self):
        return "Height: " + str(self.height) + "\nWeight: " + str(self.weight) + "\n"

class Recommended(models.Model):
    recommended_name = models.CharField(max_length=50)
    
    def __str__(self):
        return "Name: " + str(self.recommended_name)

class Workout(models.Model):
    recommended_programs = models.ManyToManyField(Recommended)
    workout_program = models.CharField(max_length=50)

    def __str__(self):
        return "Workout Program: " + str(self.workout_program)

    
