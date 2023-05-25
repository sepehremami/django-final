from django import template

register = template.Library()


def assistant(obj):
    string = ''
    children = obj.category_set.all()
    if children.count() == 0:
        string = '<li>{}</li>'.format(obj)
    else:
        string += fcategory(obj)

    return string


@register.filter(name='fcategory')
def fcategory(unit):
    children = unit.category_set.all()
    if children.count() == 0:
        string = '<li>{}</li>'.format(unit)
    else:
        string = '<li>{}<ul>'.format(unit)
        for child in children:
            string += assistant(child)
        string += '</ul></li>'
    return string



from math import ceil



@register.filter(name="as_chunk")
def as_chunks(lst, chunk_size):
    limit = ceil(len(lst) / chunk_size)
    for idx in range(limit):
        yield lst[chunk_size * idx : chunk_size * (idx + 1)]