from django.db import models

# CREAT ARTICLES CLASS
class Articles(models.Model):
    title = models.CharField('Name of article ', max_length=50)
    anonse = models.CharField('Anonse ', max_length=250)
    absolute_text = models.TextField('Absolute article text ')
    date = models.DateTimeField('Date of public ')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'New'
        verbose_name_plural = 'News'