from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

import markdown as md

register = template.Library()

@register.filter()
@stringfilter
def markdownRender(value):
    extensions = ["fenced_code",
        "codehilite", 
        "tables",
        "toc",
        "attr_list",
        "sane_lists",
        "smarty",
        "nl2br",
        "footnotes",
        "admonition",
        "pymdownx.superfences",
        "pymdownx.tasklist",
        "pymdownx.magiclink",
        "pymdownx.emoji",
        "pymdownx.tilde",
        "pymdownx.details",
        "pymdownx.mark",]
    extensionsConf = {"codehilite": {"guess_lang": False, "css_class": "highlight"}}
    html = md.markdown(value,
        extensions=extensions,
        extension_configs=extensionsConf,
        tab_length=4,
        output_format="html")

    return mark_safe(html)    
