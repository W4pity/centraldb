from django.shortcuts import render
from django.http import HttpResponse

def home(request):
  return render(request, 'centraldb/home.html');
def test(request):
  return render(request, 'centraldb/test.html');
