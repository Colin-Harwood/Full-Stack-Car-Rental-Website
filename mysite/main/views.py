from django.shortcuts import render
from django.contrib import messages
from datetime import datetime
from .models import BookingDetails
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return render(request, 'home.html', {})

def book(request):
    return render(request, 'book.html', {})

def fleet(request):
    return render(request, 'fleet.html', {})

def newBookingDetails(request):
    return render(request, 'newBookingDetails.html', {})

def viewBooking(request):
    if request.method == "POST":
        bookingDetail = BookingDetails.objects.get(email=request.POST.get('email'))
        print(bookingDetail)
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

        return HttpResponseRedirect(reverse('viewBooking'))
    return render(request, 'newBookingPay.html', {})

def viewBookingDetails(request, booking_id=None):
    if booking_id:
        # Query the database for the booking with the given ID
        bookings = BookingDetails.objects.filter(id=booking_id)
    else:
        # Get the email parameter from the GET request
        email = request.GET.get('email')

        # Query the database for all bookings with the given email
        bookings = BookingDetails.objects.filter(email=email)

    # Pass the bookings to the template
    return render(request, 'bookingDetails.html', {'bookings': bookings})

def delete_booking(request, booking_id):
    if request.method == 'POST':
        print("Delete booking", booking_id)
        booking = get_object_or_404(BookingDetails, id=booking_id)
        booking.delete()
        messages.success(request, 'Booking deleted successfully')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    
def update_booking(request, booking_id):
    print("Update booking", booking_id)
    if request.method == 'POST':
        if 'firstName' in request.POST:
            print("Update booking", booking_id)
            print("Update booking", request.POST['firstName'])
            booking = get_object_or_404(BookingDetails, id=booking_id)
            booking.firstName = request.POST['firstName']
            booking.lastName = request.POST['lastName']
            booking.email = request.POST['email']
            booking.phone = request.POST['phone']
            booking.pickUp = request.POST['pickUpLocation']
            booking.dropOff = request.POST['dropOffLocation'] 

            pickUp = datetime.strptime(request.POST['pickUp'], '%Y-%m-%dT%H:%M')

            booking.date = pickUp.date()
            booking.time = pickUp.time()
            
            # Update other fields in a similar way
            booking.save()
            return JsonResponse({'status': 'success'})
        else:
            booking = get_object_or_404(BookingDetails, id=booking_id)
            booking.vehicle = request.post['vehicle']
            booking.price = request.post['price']
        
    
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
    

@csrf_exempt
def update_car_and_price(request, booking_id):
    if request.method == 'POST':
        car = request.POST['car']
        price = request.POST['price']

        booking = get_object_or_404(BookingDetails, id=booking_id)
        # Update the database
        # This is just a placeholder, update it to match your actual database update logic
        booking.vehicle = car
        booking.price = price

        booking.save()

        return JsonResponse({'status': 'success'})