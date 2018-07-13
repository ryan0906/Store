from django.db import models


class Dishes(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    price = models.IntegerField()
    code = models.CharField(max_length=10)

    # def __repr__(self):
    #     return self.price


class Account(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)


class Data(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    bill = models.IntegerField()
    cashier = models.ForeignKey(Account, on_delete=models.CASCADE)
    # json structure: { "BCCC1": 1, "BCG2": 3 }
    details = models.CharField(max_length=10000)

