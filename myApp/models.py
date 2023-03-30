from django.db import models

# Create your models here.
class Post(models.Model):
    article = models.CharField(max_length=200)
    text = models.TextField()
    pub_date = models.DateTimeField('date published')
    # image = models.ImageField('image', upload_to=('../static/img'))

    def __str__(self):
        return self.article