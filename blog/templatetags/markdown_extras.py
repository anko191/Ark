from django import template
from django.template.defaultfilters import stringfilter
import markdown as md

register = template.Library()

# https://yuki.world/django-markdown-implement/
# <div id = "content"><p style = "margin-left:30px;font-size:21px;" >{{ post.text|markdown|safe }}</p></div></div>
# div id contentで出来たわ！！
@register.filter()
@stringfilter
def markdown(value):
    return md.markdown(value, extensions = ['markdown.extensions.fenced_code', 'tables'])
