from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import PhoenixForms
from .models import Puns, Thoughts, DiaryEntry

# Create your views here.

def user_login(request):

    '''This function is intended for when the user logs in, they are 
    taken directly to index.html file without requesting any input.'''

    return render(request, 'index.html')

def authenticate_user(request):

    '''The user is authenticated. The username and password are requested,
    from the previous file and if successfully authenticated, the
    system will proceed to home.html, if not the system will loop back
    to the current page'''

    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)

    if user is None:
        return redirect('Personal:login')
    else:
        login(request, user)
        return render(request, 'home.html')


def account_creation(request):

    '''When prompted the system will fetch PhoenixForm and will required,
    to enter their details before proceeding, else the system will loop
    to the the PhoenixForm and repeat process'''

    if request.method == 'POST':
        form = PhoenixForms(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully.")
            return render(request, 'home.html')
    else:
        form = PhoenixForms()
    return render(request, 'Register.html', {'form': form})

def phoenixDiary(request):

    '''Diary entries are fetched and sorted by the latest entry, thus
    taking the final results to the PhoenixDiary.html. In a case where
    none entries where found, the appropriate message will be displayed'''

    Latest_diary = DiaryEntry.objects.order_by('-pub_date')[:5]
    return render(request, "PhoenixDiary.html", {
    'Latest_diary': Latest_diary,
    })

def jokes(request):

    '''Jokes contents are fetched and sorted by the latest content, thus
    taking the final results to the puns.html. In a case where
    none contents where found, the appropriate message will be displayed'''

    Latest_pun = Puns.objects.all()
    return render(request, "puns.html", {
    'Latest_pun': Latest_pun,
    })

def thoughts(request):

    '''Thoughts contents are fetched and sorted by the latest content, thus
    taking the final results to the thoughts.html. In a case where
    none contents where found, the appropriate message will be displayed'''

    Latest_thoughts = Thoughts.objects.order_by('-pub_date')[:5]
    return render(request, "thoughts.html", {
    'Latest_thoughts': Latest_thoughts,
    })