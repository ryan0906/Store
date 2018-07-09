from django.db import models


class Dishes(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    price = models.IntegerField()
    code = models.CharField(max_length=10)


class User(models.Model):
    id = models.CharField(max_length=5, primary_key=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)


class Data(models.Model):
    date = models.DateTimeField()
    cash = models.IntegerField()
    cashier = models.ForeignKey(User, on_delete=models.CASCADE)
    # json structure: { "BCCC1": 1, "BCG2": 3 }
    details = models.CharField(max_length=10000)