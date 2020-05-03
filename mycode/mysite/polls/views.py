# from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return HttpResponse("ここを変更すればブラウザの表示が変わる.")
# Create your views here.
