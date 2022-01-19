from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.


def home(request):
    # return HttpResponse("None :D lol")
    return render(request, "generator/home.html", {'password': 'random_password:'})


def eggs(request):
    return HttpResponse("big balls")


def password(request):
    characters = []
    alphabet = list("abcdefghijklmnopqrstuvwxyz")

    lower_characters = list("abcdefghijklmnopqrstuvwxyz")

    upper_characters = []
    for char in alphabet:
        upper_characters.append(char.upper())

    if request.GET.get('lowerOnes'):
        characters.extend(lower_characters)

    if request.GET.get('upperSHIT'):
        characters.extend(upper_characters)

    if request.GET.get('specialu'):
        characters.extend(list("!@#$%^&*_-+=?"))

    if request.GET.get('ambiguu'):
        characters.extend(list("()[]{};:|,<.>/'"))

    if request.GET.get('numbers'):
        characters.extend(list("0123456789"))

    length = int(request.GET.get('Characters', 16))
    thepassword = ''
    try:
        for x in range(length):
            thepassword += random.choice(characters)
        return render(request, "generator/password.html", {'password': thepassword})
    except IndexError:
        return render(request, 'generator/password.html', {'error': 'Please select at least one option.'})


def about_us(request):
    name = "Marceeeel Paaaveeel"
    citizanship = "citizan"
    age = 91
    # return HttpResponse(f"The big balls of our {age} years old {citizanship} {name} made this happen")
    context = {
        "name": name,
        "citizanship": citizanship,
        "age": age
    }
    return render(request, "generator/about_us.html", context)
