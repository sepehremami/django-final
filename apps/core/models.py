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

from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission

class Command(BaseCommand):
    help = 'Creates the "customer" group with the desired permissions'

    def handle(self, *args, **options):
        # Create the "customer" group
        customer_group, created = Group.objects.get_or_create(name='customer')

        # Add the "add_wishlist" permission to the "customer" group
        add_wishlist_permission = Permission.objects.get(codename='add_wishlist')
        customer_group.permissions.add(add_wishlist_permission)

        # Remove the "delete_wishlist" permission from the "customer" group
        delete_wishlist_permission = Permission.objects.get(codename='delete_wishlist')
        customer_group.permissions.remove(delete_wishlist_permission)

        # Save the changes to the "customer" group
        customer_group.save()

        self.stdout.write(self.style.SUCCESS('Successfully created the "customer" group with the desired permissions.'))
