from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Company(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.CharField(max_length=256)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        # uncomment if you don't want slug to update when name updates
        #if self.id is None:
            #self.slug = slugify(self.name)
        self.slug = slugify(self.name)
        super(Company, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User)

    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __unicode__(self):
        return self.user.username
