from django.shortcuts import render
from django.views.generic.list import ListView
from studentorg.models import Organization

class HomePageView(ListView):
    model = Organization
    context_object_name = 'home' # This will pass the list of organizations as 'home' to home.html
    template_name = "home.html"

class OrganizationList(ListView):
    model = Organization
    context_object_name = 'organization' # This will pass the list of organizations as 'organization' to org_list.html
    template_name = 'org_list.html'
    paginate_by = 5