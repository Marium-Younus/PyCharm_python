from django.db import models
from embed_video.fields import EmbedVideoField
class Video(models.Model):
    title = models.CharField(max_length=100)
    added = models.DateTimeField(auto_now_add=True)
    url = EmbedVideoField()

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ['-added']
class u_contact(models.Model):
    c_id = models.AutoField(primary_key=True)
    c_name = models.CharField(max_length=50)
    c_email = models.CharField(max_length=50)
    c_subject = models.CharField(max_length=100)
    c_message = models.CharField(max_length=100)

class Book(models.Model):
    book_title = models.CharField(max_length=100)
    book_author = models.CharField(max_length=100)
    book_desc = models.CharField(max_length=250)
    book_image=models.FileField(upload_to="book/")
    pdf = models.FileField(upload_to='books/pdfs/')

    def __str__(self):
        return str(self.book_title)

    def __str__(self):
        return str(self.book_author)

    def __str__(self):
        return str(self.book_desc)