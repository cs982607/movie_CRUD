from django.db import models

class Movie(models.Model):
    name         = models.CharField(max_length=50)
    country      = models.CharField(max_length=50, null=True)
    main_image   = models.URLField(max_length=200)
    description  = models.TextField(null=True)
    show_time    = models.IntegerField(null=True)
    genre        = models.CharField(max_length=50, null=True)
    director     = models.CharField(max_length=50, null=True)
    actor        = models.CharField(max_length=50, null=True)

    class Meta:
        db_table = 'movies'
