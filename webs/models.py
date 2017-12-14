from django.db import models

class Web(models.Model):
    name = models.CharField(max_length=50)
    open = models.FloatField()
    close = models.FloatField()
    income = models.FloatField()
    openYear = models.IntegerField()
    NoOfEmploy = models.IntegerField(default=2)

    def __str__(self):
        return self.name
