# Create your views here.

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template import loader
from django.contrib.auth import logout as auth_logout

from .models import Artist, Album
from .forms import 