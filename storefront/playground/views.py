from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def say_helloworld(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())