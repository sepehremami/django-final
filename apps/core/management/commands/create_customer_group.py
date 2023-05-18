from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
class Command(BaseCommand):
    help = 'Creates the "customer" group with the desired permissions'
    name = 'create_customer_group'

    def handle(self, *args, **options):
        # Create the "customer" group
        customer_group, created = Group.objects.get_or_create(name='customer')

        # Add the "add_wishlist" permission to the "customer" group
        add_wishlist_permission = Permission.objects.get(codename='view_product')
        add_wishlist_permission = Permission.objects.get(codename='add_category')
        customer_group.permissions.add(add_wishlist_permission)

        # Remove the "delete_wishlist" permission from the "customer" group
        delete_wishlist_permission = Permission.objects.get(codename='delete_product')
        customer_group.permissions.remove(delete_wishlist_permission)

        # Save the changes to the "customer" group
        customer_group.save()

        self.stdout.write(self.style.SUCCESS('Successfully created the "customer" group with the desired permissions.'))
