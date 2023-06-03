from django import template
from apps.shop.models import Category
register = template.Library()


def assistant(obj):
    string = ''
    children = obj.category_set.all()
    if children.count() == 0:
        string = '<li><a href="{}">{}</a></li>'.format(obj.get_absolute_url(), obj)
    else:
        string += fcategory(obj)

    return string


@register.filter(name='fcategory')
def fcategory(unit:Category):
    children = unit.category_set.all()
    # if children.count() == 0:
    #     # string = '<li>{}</li>'.format(unit)
    #     string = "<li><a href='{}'>{}</a></li>".format(unit.get_absolute_url(), unit.name)
    # else:
    string = '<li><a href="{}">{}<ul>'.format(unit.get_absolute_url(),unit)
    for child in children:
        string += assistant(child)
    string += '</ul></a></li>'
    return string


