from django.db import models
from django.urls import reverse


# Create your models here.


class Travel(models.Model):
    destination = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    user_id = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        """A string representation of the model."""
        return self.destination[:50]

    def get_absolute_url(self):
        return reverse('home')

    

