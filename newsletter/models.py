from django.db import models


class Newsletter(models.Model):
    '''
    Model for newsletter
    '''

    class Meta:
        ordering = ('-date',)


    title = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.title
