from django.db import models

class Conges(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateField()
    end_date = models.DateField()
    REASONS = [
    ('conges_payes', 'Congés Payés'),
    ('conges_maladie', 'Congés Maladie'),
    ('conges_exceptionnels', 'Congés Exceptionnels'),]
    reason = models.CharField(max_length=20, choices=REASONS, default='conges_payes')
    validate = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.name} {self.lastname}"
