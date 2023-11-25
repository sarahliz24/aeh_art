from django.db import models


class Publications(models.Model):

    class Meta:
        ordering = ('-publication_year',)
        verbose_name = 'Publications'
        verbose_name_plural = 'Publications'

    title = models.CharField(max_length=150)
    authors = models.CharField(max_length=500)
    publication_year = models.IntegerField()
    source = models.CharField(max_length=150, null=True, blank=True)
    volume_number = models.CharField(max_length=20, null=True, blank=True)
    page_range = models.CharField(max_length=500, null=True, blank=True, default="n/a")
    doi = models.CharField(max_length=150, null=True, blank=True)
    link_url = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.title
