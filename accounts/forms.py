from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class SignupForm(forms.ModelForm):
    password = forms.CharField(min_length=8, widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', 'confirm_password', 'telephone', 'address1']

    def clean(self):
        cleaned_data = super(SignupForm, self).clean()

        if any(self.errors):
            return self.errors

        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
                raise forms.ValidationError(
                "Passwords don't match"
            )

        return self.cleaned_data
