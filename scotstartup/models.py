from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.utils import timezone

class Company(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.CharField(max_length=256)
    slug = models.SlugField()
    created = models.DateTimeField(editable=False, default=timezone.now)
    modified = models.DateTimeField(default=timezone.now)
    featured = models.BooleanField(default="false")

    def save(self, *args, **kwargs):
        # uncomment if you don't want slug to update when name updates
        #if self.id is None:
            #self.slug = slugify(self.name)
        self.slug = slugify(self.name)
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        
        super(Company, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.CharField(max_length=256)
    slug = models.SlugField()
    created = models.DateTimeField(editable=False, default=timezone.now)
    modified = models.DateTimeField(default=timezone.now)
    featured = models.BooleanField(default="false")

    def save(self, *args, **kwargs):
        # uncomment if you don't want slug to update when name updates
        #if self.id is None:
            #self.slug = slugify(self.name)
        self.slug = slugify(self.name)
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        
        super(Event, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User)

    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __unicode__(self):
        return self.user.username
