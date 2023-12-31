from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {})

def book(request):
    return render(request, 'book.html', {})

def fleet(request):
    return render(request, 'fleet.html', {})

def newBookingDetails(request):
    return render(request, 'newBookingDetails.html', {})

def viewBooking(request):
    return render(request, 'viewBooking.html', {})

def newBookingVehicle(request):
    return render(request, 'newBookingVehicle.html', {})

def newBookingPay(request):
    return render(request, 'newBookingPay.html', {})