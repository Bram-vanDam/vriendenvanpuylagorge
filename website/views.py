from django.views.generic import TemplateView
from django_ratelimit.decorators import ratelimit
from django.shortcuts import render
import json
# Home page view
class HomePageView(TemplateView):
    template_name = r'homepage.html'
class AnimatieView(TemplateView):
    template_name = r'animatie.html'
class StichtingView(TemplateView):
    template_name = r'stichting.html'
class VrijwilligersView(TemplateView):
    template_name = r'vrijwilligers.html'
class SponsoringView(TemplateView):
    template_name = r'sponsoring.html'










