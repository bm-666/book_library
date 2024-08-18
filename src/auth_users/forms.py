from library.models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from django import forms

class CustomCreateUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = '__all__'

class BaseSinOutForm(forms.ModelForm):
    """базовая форма регистрации с общими полями и методами"""
    username = forms.CharField(help_text='')
    email = forms.EmailField(label='Email')
    password = forms.CharField(help_text='', label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(help_text='', label='Confirm password', widget=forms.PasswordInput)


    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password != password2:
            raise forms.ValidationError("Пароли не совпадают")


class LibrarianSignOutForm(BaseSinOutForm):
    """форма регистрации для библиотекаря"""
    employee_id = forms.CharField()

    class Meta:
        model = CustomUser
        fields = ['username', 'email','employee_id','role', 'password']

class ReaderSingOutForm(BaseSinOutForm):
    """форма регистрации для читателя"""
    first_name = forms.CharField(required=True, min_length=2)
    last_name = forms.CharField(required=True, min_length=2)
    address = forms.CharField(required=True, min_length= 10)

    class Meta:
        model = CustomUser
        fields = ['username', 'email','first_name', 'last_name',  'address', 'role', 'password', ]

class SignInForm(forms.Form):
    """форма авторизации"""
    username = forms.CharField(help_text='', label='Логин')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)