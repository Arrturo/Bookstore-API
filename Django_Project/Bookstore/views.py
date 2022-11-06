from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


def view_test1(request):
    return HttpResponse('Siema jakoś działam')