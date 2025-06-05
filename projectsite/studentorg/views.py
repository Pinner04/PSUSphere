from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from studentorg.models import Organization, OrgMember, Student, College
from studentorg.forms import OrganizationForm, OrgMemberForm, StudentForm, CollegeForm
from django.urls import reverse_lazy
from django.db.models import Q

class HomePageView(ListView):
    model = Organization
    context_object_name = 'home' # This will pass the list of organizations as 'home' to home.html
    template_name = "home.html"

class OrganizationList(ListView):
    model = Organization
    context_object_name = 'organization' # This will pass the list of organizations as 'organization' to org_list.html
    template_name = 'org_list.html'
    paginate_by = 5

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        query = self.request.GET.get('q')
        if query:
            return qs.filter(
                Q(name__icontains=query) |
                Q(description__icontains=query) |
                Q(college__college_name__icontains=query) # Assuming you want to search by college name
            )
        return qs

class OrganizationCreateView(CreateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_add.html'
    success_url = reverse_lazy('organization-list')

class OrganizationUpdateView(UpdateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_edit.html'
    success_url = reverse_lazy('organization-list')

class OrganizationDeleteView(DeleteView):
    model = Organization
    template_name = 'org_del.html'
    success_url = reverse_lazy('organization-list')

class OrgMemberList(ListView):
    model = OrgMember
    context_object_name = 'orgmember_list'
    template_name = 'orgmember_list.html' # You'll need to create this template
    paginate_by = 10

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        query = self.request.GET.get('q')
        if query:
            # Search by student's last name, first name, or organization name
            return qs.filter(
                Q(student__lastname__icontains=query) |
                Q(student__firstname__icontains=query) |
                Q(organization__name__icontains=query)
            )
        return qs

class OrgMemberCreateView(CreateView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = 'orgmember_add.html' # You'll need to create this template
    success_url = reverse_lazy('orgmember-list') # Assumes you'll name this URL pattern 'orgmember-list'

class OrgMemberUpdateView(UpdateView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = 'orgmember_edit.html' # You'll need to create this template
    success_url = reverse_lazy('orgmember-list')

class OrgMemberDeleteView(DeleteView):
    model = OrgMember
    template_name = 'orgmember_del.html' # You'll need to create this template
    success_url = reverse_lazy('orgmember-list')

class StudentList(ListView):
    model = Student
    context_object_name = 'student_list'
    template_name = 'student_list.html'
    paginate_by = 10

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        query = self.request.GET.get('q')
        if query:
            # Search by student ID, lastname, firstname, or program name
            return qs.filter(
                Q(student_id__icontains=query) |
                Q(lastname__icontains=query) |
                Q(firstname__icontains=query) |
                Q(program__prog_name__icontains=query)
            )
        return qs

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_add.html'
    success_url = reverse_lazy('student-list')

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_edit.html'
    success_url = reverse_lazy('student-list')

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student_del.html'
    success_url = reverse_lazy('student-list')

class CollegeList(ListView):
    model = College
    context_object_name = 'college_list'
    template_name = 'college_list.html'
    paginate_by = 10

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        query = self.request.GET.get('q')
        if query:
            return qs.filter(college_name__icontains=query)
        return qs

class CollegeCreateView(CreateView):
    model = College
    form_class = CollegeForm
    template_name = 'college_add.html'
    success_url = reverse_lazy('college-list')

class CollegeUpdateView(UpdateView):
    model = College
    form_class = CollegeForm
    template_name = 'college_edit.html'
    success_url = reverse_lazy('college-list')

class CollegeDeleteView(DeleteView):
    model = College
    template_name = 'college_del.html'
    success_url = reverse_lazy('college-list')