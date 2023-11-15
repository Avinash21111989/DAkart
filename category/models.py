from django.urls import reverse

from django.db import models

# Create your models here.

class Category(models.Model):
  category_name = models.CharField(max_length=100, unique= True)
  url = models.CharField(max_length=100, unique= True)
  description = models.TextField(max_length=500, blank= True)
  category_image = models.ImageField(upload_to='images/categories', blank= True)

  class Meta():
    verbose_name = 'category'
    verbose_name_plural = 'categories'

  def get_url(self):
    return reverse('products_by_category', args = [self.url])

  def __str__(self):
    return self.category_name




