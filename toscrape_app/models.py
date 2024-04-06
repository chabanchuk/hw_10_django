from django.db import models

# Create your models here.

class Author(models.Model):
    fullname = models.CharField(max_length=200)
    born_date = models.CharField(max_length=200)
    born_location = models.CharField(max_length=200)
    description = models.TextField()
    def __str__(self) -> str:
        return self.fullname

class Quote(models.Model):
    quote = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.JSONField(default=list)
    def __str__(self) -> str:
        return self.quote 