from django.shortcuts import render
import random


def home(request):
    password_length = range(8, 16)
    return render(request, 'password_generator/home.html', {'password_length': password_length})


def password(request):
    Chars = list('abcdefghijklmnopqrstuvwxyz')
    length_password = int(request.GET.get('length', 8))

    if request.GET.get('uppercase'):
        Chars += ''.join(Chars).upper()

    if request.GET.get('numbers'):
        Chars.extend(list('0123456789'))

    if request.GET.get('special_char'):
        Chars.extend(list('~!@#$%^&*()+\'`;:<>/\|'))

    the_password = ''
    for char in range(length_password):
        the_password += random.choice(Chars)

    return render(request, 'password_generator/password.html', {'password': the_password})

