from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.db.models.signals import post_save

# Create your models here.


class Profile(models.Model):
    GENDERS = (
        ('male', 'Male'),
        ('female', 'Female')
    )
    user = models.OneToOneField(User, related_name='user')
    gender = models.CharField(max_length=20, null=True, blank=True, choices=GENDERS, default='Select Gender')
    photo = models.ImageField(verbose_name='Profile Picture', upload_to='profiles/%Y/%m/%d', null=True, blank=True)
    website = models.URLField(default='', blank=True)
    bio = models.TextField(default='', blank=True)
    phone = models.CharField(max_length=20, blank=True, default='')
    city = models.CharField(max_length=100, default='', blank=True)
    country = CountryField(default='Select Country')
    organization = models.CharField(max_length=100, default='', blank=True)
    is_tasker = models.BooleanField(default=True)
    is_expert = models.BooleanField(default=False)

    def __str__(self):
        return u'%s %s' % (self.user.first_name, self.user.last_name)


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)