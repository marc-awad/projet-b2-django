from django.db import models

class Conges(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()

    def __str__(self):
        return f"{self.name} {self.lastname}"
