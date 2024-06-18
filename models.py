from django.db import models

# Create your models here.

genders = {
    "M": "Male",
    "F": "Famele"
}
class HumanInfo(models.Model):
    firts_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()

    class Meta:
        abstract = True


class Parent(HumanInfo):
    gender = models.CharField(max_length=100, choices=genders)


class Child(HumanInfo):
    parents = models.ForeignKey(Parent, on_delete=models.CASCADE)


class Icecream(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()


class Kiosk(models.Model):
    name = models.CharField(max_length=100)
    icecreams = models.ForeignKey(Icecream, on_delete=models.CASCADE)


