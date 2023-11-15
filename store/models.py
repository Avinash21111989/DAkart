from django.db import models
from django.urls import reverse
from category.models import Category

# Create your models here.
class Product(models.Model):
  product_name = models.CharField(max_length= 300, unique= True)
  slug = models.SlugField(max_length= 100, unique= True)
  description = models.TextField(max_length= 500, unique= True)
  price = models.FloatField()
  images = models.ImageField(upload_to='images/products')
  stock = models.IntegerField()
  category = models.ForeignKey(Category, on_delete= models.CASCADE)
  created_date = models.DateField(auto_now_add=True)
  modified_date = models.DateField(auto_now_add=True)
  is_available = models.BooleanField(default=True)

  def get_url(self):
    return reverse('products_detail', args=[self.category.url, self.slug])

  def __str__(self):
    return self.product_name

class VariationManager(models.Manager):
  def colors(self):
    return super(VariationManager,self).filter(variation_category__iexact='color')
  
  def sizes(self):
    return super(VariationManager,self).filter(variation_category__iexact='size')


variation_category_choices = [
                                ('color','color'),
                                ('size','size')
                              ]

class Variation(models.Model): #creating another table for choosing different colors for product for redundancy
  product = models.ForeignKey(Product,on_delete=models.CASCADE)
  variation_category = models.CharField(max_length=100,choices=variation_category_choices)
  variation_value = models.CharField(max_length=100)
  is_active = models.BooleanField(default=True)
  created_date = models.DateField(auto_now_add=True)
  objects=VariationManager()
  def __str__(self):
    # return self.product.product_name
    return self.variation_value