from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context_dict = {'message': 'skilabod!'}
    return render(request , "verkefni/index.html", context = context_dict)
