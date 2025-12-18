from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    birth_date = models.DateField()

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books'
    )
    published_date = models.DateField()
    isbn =models.CharField(max_length=13, unique=True)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    cover_image = models.ImageField(upload_to='book_covers/', null=True, blank=True)
    def __str__(self):
        return self.title

class Borrower(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    borrowed_books = models.ManyToManyField(Book, blank=True)

    def __str__(self):
        return self.name