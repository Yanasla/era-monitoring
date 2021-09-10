from django.shortcuts import render

def btest_home(request):
    return render(request, 'btest/btest_home.html')