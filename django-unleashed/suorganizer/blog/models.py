from django.db import models
from organizer.models import Startup, Tag

class Post(models.Model):
    tags = models.ManyToManyField(Tag)
    startups = models.ManyToManyField(Startup)
    title = models.CharField(max_length=63)
    slug = models.SlugField()
    text = models.TextField()
    pub_date = models.DateField()
