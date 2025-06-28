from django import template
from ..code.custom_form_data import return_survey_links
from django.http import HttpRequest

register = template.Library()

@register.simple_tag
def get_survey_links(category):
    request = HttpRequest()
    request.GET = {'category': category}
    return return_survey_links(request)