from django.db import models

# Create your models here.
class Author(models.Model):
    AuthorID = models.IntegerField(primary_key = True)
    Name = models.CharField(max_length = 40)
    Age = models.IntegerField(max_length = 4)
    Country = models.CharField(max_length = 40)

class Book(models.Model):
    ISBN = models.IntegerField(primary_key = True)
    Title = models.CharField(max_length = 40)
    AuthorID = models.ForeignKey(Author)
    Publisher = models.CharField(max_length = 40)
    PublishDate = models.DateTimeField()
    Price = models.IntegerField(max_length = 40)