from django.db import models

class Race(models.Model):
    raceName = models.CharField(max_length=255, blank=False)
    
    def __str__(self):
            return self.raceName

class NPC(models.Model):
    firstName = models.CharField(max_length=255, blank = False)
    lastName = models.CharField(max_length=255, blank = False)
    race = models.ForeignKey(Race, default=1, on_delete=models.CASCADE)
    aligment = models.CharField(max_length=255, blank = True)
    city = models.TextField(blank=True)
    role = models.TextField(blank=True)
    age = models.CharField(max_length=4,blank=True)
    comment = models.TextField(blank=True)

class Names(models.Model):
    name = models.CharField(max_length=255, blank=False)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)

class MaleNames(models.Model):
    maleName = models.CharField(max_length=255, blank=False)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)

class FemaleNames(models.Model):
    femaleName = models.CharField(max_length=255, blank=False)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)

class FamilyNames(models.Model):
    familyName = models.CharField(max_length=255, blank=False)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)

