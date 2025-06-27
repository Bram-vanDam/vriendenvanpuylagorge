from django.urls import path
from website.views import AnimatieView, StichtingView, VrijwilligersView, HomePageView, SponsoringView
from website.code.custom_form_data import return_survey_links   

urlpatterns = [
     path('', HomePageView.as_view(), name='home'),
     path("animatie", AnimatieView.as_view(), name="animatie"),
    path("stichting", StichtingView.as_view(), name="stichting"),
    path("vrijwilligers", VrijwilligersView.as_view(), name="vrijwilligers"),
    path("sponsoring", SponsoringView.as_view(), name="sponsoring"),

    #get survey links for given category and year
    path("surveylinks",return_survey_links, name="survey_links"),


]