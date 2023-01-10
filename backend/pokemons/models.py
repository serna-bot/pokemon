from django.db import models

# Create your models here.
class Type(models.Model):
    name = models.CharField("Name", max_length=240)

    def __str__(self):
        return self.name

class Ability(models.Model):
    name = models.CharField("Name", max_length=240)
    def __str__(self):
        return self.name

class Pokemon(models.Model):
    poke_id = models.IntegerField(default = -1)
    name = models.CharField("Name", max_length=240)
    image_url = models.URLField()
    base_experience = models.IntegerField(default = 0)
    height = models.IntegerField(default = 0)
    weight = models.IntegerField(default = 0)
    abilities = models.ForeignKey(Ability, on_delete=models.CASCADE)
    types = models.ForeignKey(Type, on_delete=models.CASCADE)
