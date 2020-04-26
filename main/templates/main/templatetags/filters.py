from django import template

register = template.Library()

@register.filter()
def range(value):
    """
    Returns a list the length of the value

    Will cast a string to an int
    """
    return list(range(int(value)))