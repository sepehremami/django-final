from django.db import models
from django.contrib.auth.models import AbstractUser
from django_jalali.db import models as jmodels
from django.contrib.auth.models import Group, Permission
from django.core.validators import RegexValidator


class BaseModel(models.Model):
    """
    Common attributes of all models
    All models extend BaseModel
    """

    is_deleted = models.BooleanField(default=False)
    create_date = jmodels.jDateField(auto_now_add=True)
    modified_date = jmodels.jDateField(auto_now=True)

    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.save()

    def hard_delete(self):
        super().delete()
