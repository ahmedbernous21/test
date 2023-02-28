from django.shortcuts import render

# Create your views here.

def hello(request):
    hello="hello world"

    return render(request, "testes/test.html", {'hello': hello})
