from typing import Any

from django import template

register = template.Library()


@register.filter(name='display')
def display_value(value: Any, arg: str = None) -> str:
    """Returns the display value of a BoundField or other form fields"""
    if not arg:  # attempt to auto-parse
        # Returning regular field's value
        if not hasattr(value.field, 'choices'): return value.value()
        # Display select value for BoundField / Multiselect field
        # This is used to get_..._display() for a read-only form-field
        # which is not rendered as Input, but instead as text
        return list(value.field.choices)[value.value()][1]

    # usage: {{ field|display_value:<arg> }}
    if hasattr(value, 'get_' + str(arg) + '_display'):
        return getattr(value, 'get_%s_display' % arg)()
    elif hasattr(value, str(arg)):
        if callable(getattr(value, str(arg))):
            return getattr(value, arg)()
        return getattr(value, arg)

    return value.get(arg) or ''
