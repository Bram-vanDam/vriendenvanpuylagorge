from ..models import SURVEY_LINKS
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
    
def return_survey_links(request):
    category= request.GET.get("category")
    print(f"DEBUG: Requested category: '{category}'")
    
    # Debug: Show all categories in database
    all_categories = set([obj.category for obj in SURVEY_LINKS.objects.all()])
    print(f"DEBUG: All categories in database: {all_categories}")
   
    survey_links= SURVEY_LINKS.objects.filter(category=category).values("name","link")
    survey_links_list= list(survey_links)
    survey_links_list= {survey_link["name"]: survey_link["link"]  for survey_link in survey_links_list}
    # return JsonResponse(json.dumps({
    #         'Google': 'https://www.google.com',
    #         'Wikipedia': 'https://www.wikipedia.org',
    #         'GitHub': 'https://www.github.com'
    #     }),safe=False)
    print(f"DEBUG: Found {len(survey_links_list)} links for category '{category}': {survey_links_list}")
    return JsonResponse(survey_links_list,safe=False)

#