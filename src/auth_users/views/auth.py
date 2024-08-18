from doctest import master

from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth import login, logout
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.shortcuts import render

from enums.Role import Role
from library.models import CustomUser
from ..forms import SignInForm, LibrarianSignOutForm, ReaderSingOutForm


# TODO сообщения ошибок вынести в enum

def sign_out(request):
    """метод  регистрации для библиотекаря и читетателя тип формы определяем с какого url пришел запрос"""
    path = request.path.split('/')[-1]

    if path == Role.LIBRARIAN:
        main_form = LibrarianSignOutForm
    elif path == Role.READER:
        main_form = ReaderSingOutForm

    if request.method == 'POST':

        form = main_form(request.POST)

        if form.is_valid():
            password = form.cleaned_data.get('password')
            new_user = form.save(commit=False)
            new_user.password = make_password(password)
            new_user.save()
            return HttpResponseRedirect('/')
    else:
        form = main_form()

    return render(request, 'forms/sign_out.html', context={'form': form})

def sign_in(request):
    """ метод авторизации общий для всех ролей"""
    if request.method != 'POST':
        return render(request, 'forms/sign_in.html', context={'form': SignInForm()})

    form = SignInForm(request.POST)

    if form.is_valid():
        try:
            user = CustomUser.objects.get(username=request.POST.get('username'))
        except ObjectDoesNotExist:
            context = {'form': form, 'error': 'Пользователь не найден'}
            return render(request, 'forms/sign_in.html', context=context)

        if not check_password(request.POST.get('password'), user.password):
            context = {'form': form, 'error': 'Введен не правильный пароль'}
            return render(request, 'forms/sign_in.html', context=context)

        login(request, user)
        return HttpResponseRedirect('/')



def user_logout(request):
    """выход из личного кабинета"""
    logout(request)
    return HttpResponseRedirect('/')
