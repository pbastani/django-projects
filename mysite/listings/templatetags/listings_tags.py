from django import template

register = template.Library()


@register.filter(name='joinby')
def joinby(value, arg):
    return arg.join(value)


@register.filter(name='addcss')
def addcss(field, css):
   return field.as_widget(attrs={"class":css})