#!/usr/bin/python
# -*- coding: Utf8 -*-
from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,Group


def index_view(request):
    return render_to_response('home/index.html',context_instance=RequestContext(request))

def menuA_view(request):
    return render_to_response('home/menuA.html',context_instance=RequestContext(request))

def menuE_view(request):
    return render_to_response('home/menuE.html',context_instance=RequestContext(request))