from ..models import SURVEY_LINKS
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
    
def return_survey_links(request):
    category = request.GET.get("category")
    print(f"DEBUG: Requested category: '{category}'")
    
    # Debug: Show all categories in database
    all_categories = set([obj.category for obj in SURVEY_LINKS.objects.all()])
    print(f"DEBUG: All categories in database: {all_categories}")
    
    # Debug: Show all objects in database
    all_objects = SURVEY_LINKS.objects.all()
    print(f"DEBUG: All objects in database:")
    for obj in all_objects:
        print(f"  - ID: {obj.id}, Name: '{obj.name}', Category: '{obj.category}', Link: '{obj.link}'")
    
    # Try case-insensitive search
    survey_links = SURVEY_LINKS.objects.filter(category__iexact=category).values("name","link")
    print(f"DEBUG: Case-insensitive search for '{category}' returned {survey_links.count()} results")
    
    # If no results, try exact match
    if not survey_links:
        survey_links = SURVEY_LINKS.objects.filter(category=category).values("name","link")
        print(f"DEBUG: Exact match search for '{category}' returned {survey_links.count()} results")
    
    # If still no results, try partial match
    if not survey_links:
        survey_links = SURVEY_LINKS.objects.filter(category__icontains=category).values("name","link")
        print(f"DEBUG: Partial match search for '{category}' returned {survey_links.count()} results")
    
    survey_links_list = list(survey_links)
    survey_links_list = {survey_link["name"]: survey_link["link"] for survey_link in survey_links_list}
    
    print(f"DEBUG: Final result for category '{category}': {survey_links_list}")
    return JsonResponse(survey_links_list, safe=False)

#