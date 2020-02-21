from django.db import models


# Create your models here.
class News(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    header = models.CharField(max_length=255)
    views = models.IntegerField(default=0)
    text = models.TextField()

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.header
