from django.db import models


class Review(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    auther = models.CharField(max_length=255)
    date = models.DateField()
    stars = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return self.title
