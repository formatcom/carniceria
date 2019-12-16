from django.db import models
from django.utils.html import format_html

class Category(models.Model):

    name = models.CharField(blank=False, max_length=150)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Product(models.Model):

    name = models.CharField(blank=False, max_length=150)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    cover = models.ImageField(upload_to="item/cover/%Y/%m/%d")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def preview(self):
        return format_html('''
        <a href="{0}" target="_blank"><img src={0} width=40px /></a>
        ''', self.cover.url,)

    def __str__(self):
        return self.name
