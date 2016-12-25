from asyncio.locks import Lock

from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model,
)

User = get_user_model()


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username and password:
            user = authenticate(username=username, password=password)

            if not user:
                print("Korisnik ne postoji")
                raise forms.ValidationError("Korisnik ne postoji")

            if not user.check_password(password):
                print("pogresan password!")
                raise forms.ValidationError("Pogresan password")

        return super(LoginForm, self).clean()
