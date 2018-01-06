from django.db import models
from DjangoUeditor.models  import   UEditorField
from django.db.models import permalink
from webproject.fields import ThumbnailImageField
from django.urls import reverse
from django.utils.html import strip_tags
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=70)
    body = UEditorField('content', height=300, width=1000,
                           default=u'', blank=True, imagePath="uploads/images/",
                           toolbars='besttome', filePath='uploads/files/')
    excerpt = models.CharField(max_length=200, blank=True)
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    views = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('website:detail', kwargs={'pk': self.pk})
    class Meta:
        ordering = ['-created_time']
    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])
    def save(self, *args, **kwargs):
        if not self.excerpt:
            self.excerpt = strip_tags(self.body)[:54]
        super(Post, self).save(*args, **kwargs)
    def __unicode__(self):
        return self.name

class Photo(models.Model):
    post = models.ForeignKey(Post)
    title = models.CharField(max_length=100)
    image = ThumbnailImageField(upload_to='photos')
    caption = models.CharField(max_length=250, blank=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    @permalink
    def get_absolute_url(self):
        return ('photo_detail', None, {'pk': self.id})