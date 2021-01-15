from django.contrib.auth.models import User
from django import forms


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Подтвердите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
        ]

    # def clean_password(self):
    #     cd = self.cleaned_data
    #     breakpoint()
    #     if cd['password'] != cd['password2']:
    #         raise forms.ValidationError('Пароли не совпадают')

