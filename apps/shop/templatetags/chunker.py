from django import template

from math import ceil

register = template.Library()

@register.filter(name="as_chunk")
def as_chunks(lst, chunk_size):
    limit = ceil(len(lst) / chunk_size)
    for idx in range(limit):
        yield lst[chunk_size * idx : chunk_size * (idx + 1)]