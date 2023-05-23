from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType


staff_group, staff_created = Group.objects.get_or_create(name='Staff')
manager_group, manager_created = Group.objects.get_or_create(name='Manager')
if manager_created:
    # Add any relevant custom permission classes.
    add_product_permission = Permission.objects.get(codename='add_product')
    manager_group.permissions.add(add_product_permission)

    # Get the content type object for the Fish model.
    fish_content_type = ContentType.objects.get(app_label='shop', model='Product')
    # Get all available permissions for this content type.
    all_fish_permissions = Permission.objects.filter(content_type=fish_content_type)
    # Retrieve the Manager group from above.
    manager_group = Group.objects.get(name='Manager')
    # Assign all fish-related permissions to manager group.
    for permission in all_fish_permissions:
        manager_group.permissions.add(permission)


if staff_created:
    add_product_permission = Permission.objects.get(codename='add_product')

    manager_group.permissions.add(add_product_permission)
