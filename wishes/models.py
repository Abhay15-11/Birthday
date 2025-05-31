from django.db import models

class BirthdayWish(models.Model):
    name = models.CharField(max_length=15)
    photo = models.ImageField(upload_to='uploads/')

    def __str__(self):
        return self.name
