from django.contrib.auth.forms import UserCreationForm
from django import forms
from django import forms
from django.core.exceptions import ValidationError
from project.models import BLOOD_TYPE, Profile


class UserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ('username', 'first_name', 'last_name', 'email')


YEARS = [x for x in range(1900,2020)]

MONTHS = {
    1:('Styczeń'), 2:('Luty'), 3:('Marzec'), 4:('Kwiecień'),
    5:('Maj'), 6:('Czerwiec'), 7:('Lipiec'), 8:('Sierpień'),
    9:('Wrzesień'), 10:('Październik'), 11:('Listopad'), 12:('Grudzień')
}


def password_validation(value):
    if len(value) < 8:
        raise ValidationError("za krótkie hasło co najmniej 8 znaków")


class UserForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput, validators=[password_validation])
    re_password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()
    first_name = forms.CharField(required=True, max_length=64)
    last_name = forms.CharField(required=True, max_length=64)
    birth_date = forms.DateField(label='What is your birth date?', widget=forms.SelectDateWidget(years=YEARS, months=MONTHS))
    blood_type = forms.ChoiceField(choices=BLOOD_TYPE)
    pesel = forms.CharField(max_length=11)

    def clean(self):
        cleaned_data = super().clean()
        if not self.errors:
            if cleaned_data['password'] != cleaned_data['re_password']:
                raise ValidationError("Hasła nie są identyczne")
        return self.cleaned_data