from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, Template, loader


def inicio(request):
    return HttpResponse("este inicio es de la view original")
    