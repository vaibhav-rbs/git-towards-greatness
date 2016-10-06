from django.db import models

class Tag(models.Model):
    name = models.CharField(
        max_length=31, unique=True)
    slug = models.SlugField(
        max_length=31,
        unique=True,
        help_text='A lable for URL config'
    )
    class Meta:
        ordering  = ['name']

    def __str__(self):
        return self.name

class Startup(models.Model):
    tags = models.ManyToManyField(Tag)
    name = models.CharField(
        max_length=31, db_index=True)
    slug = models.SlugField(
        max_length=31,
        unique=True,
        help_text='A lable for URL config.'
    )
    description = models.TextField()
    founded_date = models.DateField('date founded')
    contact = models.EmailField()
    website = models.URLField()
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
        get_latest_by = 'founded_date'
    
class NewsLink(models.Model):
    startup = models.ForeignKey(Startup)
    title = models.CharField(max_length=63)
    pub_date = models.DateField('date published')
    link = models.URLField(max_length=255)
    
    class Meta:
        verbose_name = 'news article'
        ordering = ['-pub_date']
        get_latest_by = 'pub_date'

    def __str__(self):
        return "{}:{}".format(
            self.startup, self.title)