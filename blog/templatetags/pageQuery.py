from django import template
register = template.Library()

@register.simple_tag(takes_context=True)
def querystring(context, **kwargs):
    q = context["request"].GET.copy()
    for k, v in kwargs.items():
        q[k] = v
    return "?" + q.urlencode()
