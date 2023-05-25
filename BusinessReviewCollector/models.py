from django.db import models


class Review(models.Model):
    title = models.CharField(max_length=25, help_text="Title of review")
    content = models.TextField(help_text="Content of review")
    auther = models.CharField(max_length=255, help_text="Auther of review")
    date = models.DateField(help_text="Date of Review in format January 2022")
    stars = models.DecimalField(
        max_digits=3, decimal_places=2, help_text="Rating stars of review")

    def __str__(self):
        return self.title
