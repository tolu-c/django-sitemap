from django.db import models
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.


class Snippet(models.Model):
  title = models.CharField(max_length=150)
  slug = models.SlugField(null=True, blank=True)
  body = models.TextField()

  def save(self, *args, **kwargs):
    self.slug = slugify(self.title)
    super().save(*args, **kwargs)

  def __str__(self):
        return self.title

  def get_absolute_url(self):
      return reverse("detail", kwargs={"slug": self.slug})
  
    