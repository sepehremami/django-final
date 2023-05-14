from django.db import models
from django.contrib.auth.models import AbstractUser



class BaseModel(models.Model):
    '''
    Common attributes of all modesl
    All models extend BaseModel
    '''
    is_deleted = models.BooleanField(default=False)
    create_time = models.DateField(auto_now_add=True)
    update_time = models.DateField(auto_nwo=True)

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
