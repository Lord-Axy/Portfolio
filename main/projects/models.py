from django.db import models
import os
from django.conf import settings

# img_location = os.path.join(settings.BASE_DIR, 'projectImages')


class Categories(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    alias_name = models.CharField(max_length=255,default='')

    def __str__(self):
        return self.name


class ProjectType(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    alias_name = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.name


class MiniProjects(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    github_link = models.URLField()
    description = models.TextField()
    image = models.ImageField(upload_to='projectImages')
    category = models.ForeignKey('Categories', on_delete=models.CASCADE)
    type = models.ForeignKey('ProjectType', on_delete=models.CASCADE, null=True)
    is_ml = models.NullBooleanField()
    html = models.FileField(upload_to='projectHTML', null=True, blank=True)
    tools = models.TextField(null=True, blank=True)
    dataset = models.URLField(null=True, blank=True)
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta(object):
        ordering = ['my_order']

    def __str__(self):
        return self.name