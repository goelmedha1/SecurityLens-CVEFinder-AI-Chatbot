from django.db import models


# Create your models here.
class SearchQuery(models.Model):
    search_box = models.CharField(max_length = 255)
    

    def __str__(self):
        return self.search_box
    