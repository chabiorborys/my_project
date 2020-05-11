from django.contrib.auth.models import User
from django.db import models

BLOOD_TYPE = (
    (0, "A+"),
    (1, "A-"),
    (2, "B+"),
    (3, "B-"),
    (4, "0+"),
    (5, "0-"),
    (6, "AB+"),
    (7, "AB-")
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    blood = models.IntegerField(choices=BLOOD_TYPE, null=True)
    birth_date = models.DateField(null=True)
    pesel = models.CharField(max_length=11, null=True)
    friends = models.ManyToManyField('Profile', related_name='profile_friends', symmetrical=True)


class FriendRequest(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='my_invitations')
    to_user = models.ForeignKey(User, related_name='invited', on_delete=models.CASCADE)
    accepted = models.BooleanField(default=False)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)
        if self.accepted:
            profile = Profile.objects.get(user=self.to_user)
            profile.friends.add(self.from_user.profile)
