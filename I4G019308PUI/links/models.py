from django.db import models
from . import utils
from django.contrib.auth import get_user_model

from .managers import ActiveLinkManager

# Create your models here.
class Link(models.Model):
    target_url = models.URLField(max_length=200)
    description = models.CharField(max_length=200)
    identifier = models.SlugField(blank=True, unique=True, max_length=20)
    author = models.ForeignKey(get_user_model())
    created_date = models.DateTimeField()
    active = models.BooleanField(default=True)
    objects = models.Manager()
    public =  ActiveLinkManager()
