from django.db import models
from datetime import datetime

class Sex(models.Model):
    """ A lookup table for birthsex of animal """
    sex = models.CharField(max_length=25)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sex

# Create your models here.
class Animal(models.Model):
    """An animal whose health is tracked by this app"""
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    identitynumber = models.CharField(max_length=200)
    sex = models.ForeignKey(Sex, on_delete=models.CASCADE)
    #sex = models.CharField(max_length=1, default='x')
    date_of_birth = models.DateTimeField('date of birth')
    date_added = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural = 'animals'

    def __str__(self):
        return self.firstname+" "+self.lastname +" | " + self.identitynumber

class Weight(models.Model):
    """The weight of any animal on the system"""
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    weight = models.IntegerField()
    date_recorded = models.DateTimeField('date recorded', default=datetime.now())
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
            verbose_name_plural = 'weights'

    def __str__(self):
        """ Return a string representation of the model """
        return f"{self.animal} | {self.weight}kg."
