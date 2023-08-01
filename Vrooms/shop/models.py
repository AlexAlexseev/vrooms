from django.db import models

from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',
                        args=[self.slug])

class Dopolnenie(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    dop1 = models.CharField(max_length=20)
    price_dop1 = models.DecimalField(max_digits=10, decimal_places=2)
    available_dop1 = models.BooleanField(default=False)
    prod = models.ForeignKey('Product', related_name='dopolnenies', blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', blank=True, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    weight = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    dopolnenie = models.ForeignKey(Dopolnenie, related_name='products', blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail',
                        args=[self.id, self.slug])
    
    
