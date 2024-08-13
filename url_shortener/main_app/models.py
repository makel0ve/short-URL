from django.db import models


class Url_model(models.Model):
    long_url = models.URLField()
    short_url = models.URLField()
    
    
    class Meta:
        verbose_name_plural = "URLs"
