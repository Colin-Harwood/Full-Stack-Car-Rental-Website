from django.shortcuts import render
from django.contrib import messages
from datetime import datetime
from .models import BookingDetails

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
    if request.method == "POST":
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        email = request.POST['email']
        phone = request.POST['phone']
        pickUpLocation = request.POST['pickUpLocation']
        dropOff = request.POST['dropOffLocation']
        vehicle = request.POST['vehicle']
        price = request.POST['price']
        
        pickUp = datetime.strptime(request.POST['pickUp'], '%Y-%m-%dT%H:%M')

        date = pickUp.date()
        time = pickUp.time()

        # Create the booking
        booking = BookingDetails.objects.create(firstName=firstName, lastName=lastName, email=email, phone=phone, pickUp=pickUpLocation, dropOff=dropOff, vehicle=vehicle, price=price, date=date, time=time)

        # Query the database for the booking
        saved_booking = BookingDetails.objects.filter(id=booking.id).exists()

        if saved_booking:
            print("Booking was saved successfully")
        else:
            print("Booking was not saved")

        print("names", firstName, lastName, email, phone, "pick", pickUpLocation, "drop", dropOff, "veh", vehicle, price, date, time)
        
        messages.success(request, 'Booking successful')
    return render(request, 'newBookingPay.html', {})

def viewBookingDetails(request, booking_id):
    # Query the database for the booking with the given ID
    booking = BookingDetails.objects.get(id=booking_id)

    # Pass the booking to the template
    return render(request, 'bookingDetails.html', {'booking': booking})