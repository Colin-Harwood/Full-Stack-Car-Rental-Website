from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {})

def book(request):
    return render(request, 'book.html', {})

def fleet(request):
    return render(request, 'fleet.html', {})

def newBooking(request):
    return render(request, 'newBooking.html', {})

def viewBooking(request):
    return render(request, 'viewBooking.html', {})