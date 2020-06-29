from django.db import models

from django_orm_utils.queryset import AdvancedQuerySet


class AdvancedManager(models.Manager.from_queryset(AdvancedQuerySet)):
    pass
