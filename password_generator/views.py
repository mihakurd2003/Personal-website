from django.shortcuts import render
import random


def home(request):
    password_length = range(8, 16)
    return render(request, 'password_generator/home.html', {'password_length': password_length})


def password(request):
    Chars = {
        'simple': list('abcdefghijklmnopqrstuvwxyz'),
        'upper': list('abcdefghijklmnopqrstuvwxyz'.upper()),
        'numbers': list('0123456789'),
        'special': list('~!@#$%^&*()+\'`;:<>/\|'),
    }
    length_password = int(request.GET.get('length', 8))

    the_password = ''
    if request.GET.get('uppercase'):
        the_password += random.choice(Chars['upper'])

    if request.GET.get('numbers'):
        the_password += random.choice(Chars['numbers'])

    if request.GET.get('special_char'):
        the_password += random.choice(Chars['special'])

    for char in range(len(the_password), length_password):
        the_password += random.choice(Chars['simple'])

    the_password = ''.join(random.sample(list(the_password), len(the_password)))

    return render(request, 'password_generator/password.html', {'password': the_password})
