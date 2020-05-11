"""PROJEKT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.views.generic import TemplateView
from django.conf.urls import url

from project import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path("accounts/", include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('profile/', views.MyProfile.as_view()),
    path('profile/<int:pk>', views.MyProfile.as_view(), name='view_profile_with_pk'),
    path('users/', views.Users.as_view()),
    path('family/', views.InvitationList.as_view()),
    path('add_family/<int:id>/', views.AddMember.as_view()),
    path('editprofile/<int:pk>', views.UpdateUserProfile.as_view()),
    path('add_test_inv/', views.TestInvView.as_view()),
    path('accept/<int:id>', views.AcceptInvitation.as_view()),
    path('delete_invitation/<int:id>', views.RemoveInvitation.as_view()),
    path('myfamily/', views.MyFamily.as_view()),
    path('delete_from_family/<int:id>', views.RemoveFromFamily.as_view()),

]
