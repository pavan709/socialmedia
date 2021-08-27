from django.db import models
from django.utils.text import slugify
# Create your models here.
import misaka
from django.urls import reverse

from django.contrib.auth import get_user_model

User = get_user_model()

from django import template

register = template.Library()


class Group(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    description = models.TextField(blank=True, default='')
    members = models.ManyToManyField(User, through='GroupMember')
    # this link is about through
    # https: // docs.djangoproject.com / en / 3.0 / ref / models / fields /  # django.db.models.ManyToManyField.through


    # this is for manytomany
    # https: // docs.djangoproject.com / en / 3.1 / topics / db / examples / many_to_many /
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('groups:single', kwargs={'slug': self.slug})

    # this link is about ordering
    # https://docs.djangoproject.com/en/3.1/ref/models/options/#ordering
    class Meta:
        ordering = ['name']


class GroupMember(models.Model):
    group = models.ForeignKey(Group, related_name='memberships',on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user_groups',on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ('group', 'user')