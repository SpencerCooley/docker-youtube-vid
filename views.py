from django.shortcuts import render
def home(request):
  c = {}
  response = render(request, 'home.html', c )
  return response
