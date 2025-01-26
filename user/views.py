from django.shortcuts import render, redirect
from django.contrib import messages
from admin_site.forms import *
from user.models import *
from django.contrib.auth.hashers import check_password
from .models import *

# Validation user
from admin_site.middleware import *

# Create your views here.
def index(request):
    usuarios = Usuario.objects.all()
    authenticate = 'user_id' in request.session
    return render(request, "user_blog/index.html", {'usuarios': usuarios, 'authenticate': authenticate})