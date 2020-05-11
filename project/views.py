from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import UpdateView, CreateView
from project.models import Profile, FriendRequest
from django.contrib.auth.models import User


class MyProfile(View):
    def get(self, request, pk=None):
        if pk:
            user = User.objects.get(pk=pk)
        else:
            user = request.user
        return render(request, 'myprofile.html', {'user_temp': user})


class MyFamily(View):
    def get(self, request):
        return render(request, 'myfamily.html')


class RemoveFromFamily(View):
    def get(self, request, id):
        user = User.objects.get(pk=id)
        request.user.profile.friends.remove(user.profile)
        return redirect('/myfamily/')


class Users(View):
    def get(self, request):
        users = User.objects.exclude(id=request.user.id).order_by("last_name")
        return render(request, 'users.html', {'users': users})


class UpdateUserProfile(UserPassesTestMixin, UpdateView):
    model = Profile
    success_url = '/profile'
    fields = ['blood', 'birth_date', 'pesel']
    template_name = 'UpdateProfile.html'

    def test_func(self):
        return self.request.user.profile.id == self.kwargs['pk']


class AddMember(View):
    def get(self, request, id):
        to_user = User.objects.get(pk=id)
        FriendRequest.objects.create(
            from_user=request.user, to_user=to_user
        )
        return redirect('/users/')


class InvitationList(View):
    def get(self, request):
        invitations = FriendRequest.objects.filter(to_user=request.user, accepted=False)
        return render(request, 'invitation_list.html', {'invitations': invitations})


class AcceptInvitation(View):
    def get(self, request, id):
        invitation = FriendRequest.objects.get(pk=id)
        invitation.accepted = True
        invitation.save()
        return redirect('/family/')


class RemoveInvitation(View):
    def get(self, request, id):
        invitation = FriendRequest.objects.get(pk=id)
        invitation.delete()
        return redirect('/family/')


class TestInvView(CreateView):
    model = FriendRequest
    template_name = 'add_inv_test.html'
    fields = '__all__'
    success_url = '/add_test_inv/'
