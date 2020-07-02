# django-orm-utils
Simple Django ORM utils to with custom queryset datastructure

# Usage
Using manager:
```py
from django.db import models
from django_orm_utils.manager import AdvancedManager


class Product(models.Model):
  ...
  name = models.CharField(...)
  label = models.CharField(...)
  company = models.ForeignKey(Company, ...)
  objects = AdvancedManager()
  

products = Product.objects.filter(id__in=[1,2,3,4]).indexable_values('name', 'label', 'company__name')
```
