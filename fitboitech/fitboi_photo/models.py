from django.db import models

# Create your models here.


class User(models.Model):
    # name = models.CharField(max_length=50)
    feet = models.FloatField(default=0.0)
    inches = models.FloatField(default=0.0)
    weight = models.FloatField(default=0.0)
    neck = models.FloatField(default=0.0)
    abdomen = models.FloatField(default=0.0)

    def __str__(self):
<<<<<<< HEAD
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

    
=======
        return "Feet: " + str(self.feet) + "\Inches: " + str(self.inches) + "\weight: " + str(self.weight)+ "\n"
>>>>>>> fa8339cefa54e89bb8a1936830d7576f982d2f68
