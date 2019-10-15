from django.db import models

# Create your models here.


class Search(models.Model):
    search = models.CharField(max_length=500)
    whenCreated = models.DateField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.searchma)

    class Meta:
        verbose_name_plural = 'Searches'
