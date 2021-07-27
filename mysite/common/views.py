from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from common.forms import UserForm

# Create your views here.

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
