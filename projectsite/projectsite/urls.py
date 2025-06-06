"""
URL configuration for projectsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from studentorg.views import HomePageView, OrganizationList, OrganizationCreateView, OrganizationUpdateView, OrganizationDeleteView
from studentorg import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path("admin/", admin.site.urls),
    path('', views.HomePageView.as_view(), name='home'),
    path('organization_list/', OrganizationList.as_view(), name='organization-list'),
    path('organization_list/add/', OrganizationCreateView.as_view(), name='organization-add'),
    path('organization_list/<int:pk>/',OrganizationUpdateView.as_view(), name='organization-update'),
    path('organization_list/<int:pk>/delete/', OrganizationDeleteView.as_view(), name='organization-delete'),

    path('org_members/', views.OrgMemberList.as_view(), name='orgmember-list'),
    path('org_members/add/', views.OrgMemberCreateView.as_view(), name='orgmember-add'),
    path('org_members/<int:pk>/', views.OrgMemberUpdateView.as_view(), name='orgmember-update'),
    path('org_members/<int:pk>/delete/', views.OrgMemberDeleteView.as_view(), name='orgmember-delete'),

    path('students/', views.StudentList.as_view(), name='student-list'),
    path('students/add/', views.StudentCreateView.as_view(), name='student-add'),
    path('students/<int:pk>/', views.StudentUpdateView.as_view(), name='student-update'),
    path('students/<int:pk>/delete/', views.StudentDeleteView.as_view(), name='student-delete'),

    path('colleges/', views.CollegeList.as_view(), name='college-list'),
    path('colleges/add/', views.CollegeCreateView.as_view(), name='college-add'),
    path('colleges/<int:pk>/', views.CollegeUpdateView.as_view(), name='college-update'),
    path('colleges/<int:pk>/delete/', views.CollegeDeleteView.as_view(), name='college-delete'),
]
