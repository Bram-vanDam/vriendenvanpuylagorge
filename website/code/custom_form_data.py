from ..models import SURVEY_LINKS
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt

def return_survey_links(request):
    category = request.GET.get("category")
    
    # Try case-insensitive search
    survey_links = SURVEY_LINKS.objects.filter(category__iexact=category).values("name","link")
    
    # If no results, try exact match
    if not survey_links:
        survey_links = SURVEY_LINKS.objects.filter(category=category).values("name","link")
    
    # If still no results, try partial match
    if not survey_links:
        survey_links = SURVEY_LINKS.objects.filter(category__icontains=category).values("name","link")
    
    survey_links_list = list(survey_links)
    survey_links_list = {survey_link["name"]: survey_link["link"] for survey_link in survey_links_list}
    
    return JsonResponse(survey_links_list, safe=False)

#