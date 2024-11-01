# archive/models.py
from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    pdf_file = models.FileField(upload_to='books/pdfs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('taggit.Tag', blank=True)

    def __str__(self):
        return self.title

    @property
    def average_rating(self):
        return self.ratings.aggregate(models.Avg('rating'))['rating__avg'] or 0

class Rating(models.Model):
    book = models.ForeignKey(Book, related_name='ratings', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])

    class Meta:
        unique_together = ('book', 'user')
