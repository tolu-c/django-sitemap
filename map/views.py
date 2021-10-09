from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Snippet

# Create your views here.


def index(request):
    return HttpResponse('index page')


def about(request):
    return HttpResponse('about page')


def contact(request):
    return HttpResponse('contact page')


def support(request):
    return HttpResponse('support page')


def snippet_detail(request, slug):
    snippet = get_object_or_404(Snippet, slug=slug)
    return HttpResponse(f'this is the detail for {slug}')
