from django import template

register = template.Library()


@register.simple_tag
def get_medicines(medicines):
    medicine = medicines.values_list('name',flat=True)
    return ",".join(medicine)