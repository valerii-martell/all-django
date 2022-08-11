from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext as _


class LoginForm(AuthenticationForm):
    '''Simple login form'''

    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise forms.ValidationError(
                _("This account is inactive."),
                code='inactive',
            )
        if user.username.startswith('b'):
            raise forms.ValidationError(
                _("Sorry, accounts starting with 'b' aren't welcome here."),
                code='no_b_users',
            )


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, help_text='Last Name')
    last_name = forms.CharField(max_length=100, help_text='Last Name')
    email = forms.EmailField(max_length=150, help_text='Email')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2')
