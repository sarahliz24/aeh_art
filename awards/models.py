from django.db import models


class Awards(models.Model):

    class Meta:
        ordering = ('-award_year',)
        verbose_name = 'Awards'
        verbose_name_plural = 'Awards'

    award_title = models.CharField(max_length=200)
    award_year = models.IntegerField()
    award_info = models.TextField(max_length=2000)
    

    def __str__(self):
        return self.title
