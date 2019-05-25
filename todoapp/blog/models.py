from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
class Primeiro_Migrate_SQN(models.Model):
    teste_titulo  = models.CharField(max_length=200)
    teste_texto = models.TextField()
    teste_date = models.DateTimeField(
            default=timezone.now)
    teste_date2 = models.DateTimeField(
            blank=True, null=True)
