from audioop import reverse
import datetime
from django.db import models
from django.utils import timezone


# Сущность категории
# - model: Модель категории
class Category(models.Model):
    category_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.category_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})


# Автор продукта
class Author(models.Model):
    name = models.CharField(max_length = 100)
    desc = models.TextField(max_length = 300)


# Сущность продукта
class Product(models.Model):
    product_title = models.CharField(max_length=200)
    product_text = models.CharField(max_length=200)
    product_price = models.IntegerField(default=0)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return self.product_title


# from api.models import *
# c = Category(category_text="Server", pub_date=timezone.now())
# c = Category.objects.filter(id=1)
# c.product_set.create(product_title="Scipt2", product_text="product_text", product_price="50")