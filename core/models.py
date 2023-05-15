from django.db import models
from django.contrib.auth.models import AbstractUser
from django_jalali.db import models as jmodels


class BaseModel(models.Model):
    """
    Common attributes of all modesl
    All models extend BaseModel
    """

    is_deleted = models.BooleanField(default=False, editable=False)
    create_date = jmodels.jDateField(auto_now_add=True)
    modified_date = jmodels.jDateField(auto_now=True)

    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.save()

    def hard_delete(self):
        super().delete()


class User(AbstractUser):
    pass


class Visitor(User):
    is_visitor = True

    class Meta:
        proxy = True
