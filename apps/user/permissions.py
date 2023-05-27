from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType


staff_group, staff_created = Group.objects.get_or_create(name='Staff')
manager_group, manager_created = Group.objects.get_or_create(name='Manager')
spectator, spectator_created = Group.objects.get_or_create(name='Spectator')
if manager_created:
    add_product_permission = Permission.objects.get(codename='add_product')
    manager_group.permissions.add(add_product_permission)

    product_content_type = ContentType.objects.get(app_label='shop', model='Product')
    all_product_permissions = Permission.objects.filter(content_type=product_content_type)
    manager_group = Group.objects.get(name='Manager')
    for permission in all_product_permissions:
        manager_group.permissions.add(permission)

    user_content_type = ContentType.objects.get(app_label='shop', model='user')
    all_user_permissions = Permission.objects.filter(content_type=user_content_type)
    manager_group = Group.objects.get(name='Manager')
    for permission in all_user_permissions:
        manager_group.permissions.add(permission)

    category_content_type = ContentType.objects.get(app_label='shop', model='category')
    all_category_permissions = Permission.objects.filter(content_type=category_content_type)
    manager_group = Group.objects.get(name='Manager')
    for permission in all_category_permissions:
        manager_group.permissions.add(permission)


if staff_created:
    add_product_permission = Permission.objects.get(codename='add_product')

    manager_group.permissions.add(add_product_permission)
    cart_content_type = ContentType.objects.get(app_label='shop', model='cart')
    all_cart_permissions = Permission.objects.filter(content_type=cart_content_type)
    manager_group = Group.objects.get(name='Manager')
    for permission in all_cart_permissions:
        manager_group.permissions.add(permission)

if spectator_created:
     add_product_permission = Permission.objects.get(codename='view_product')
     add_category_permission = Permission.objects.get(codename='view_category')
     add_user_permission = Permission.objects.get(codename='view_user')
     add__permission = Permission.objects.get(codename='view_all')
