from django.shortcuts import render,HttpResponse
from .models import destinations,booking,cars,Contact

# Create your views here.

def test (req):
    return HttpResponse("<h1> The application is  running </h1>")

def Home(req):
    des= destinations.objects.all()
    data={
        'des':des

    }
    return render(req,'index.html' ,  data )
 
def Menu_page(req):
    car=cars.objects.all()
    data= {

        'car':car
    }

    return render(req,'menu.html',data)

def Booking_page(req):
    Booking=booking.objects.all()
    data={
       'Booking':Booking
    }
    return render (req , 'booking.html', data )

def Contact_page(req):
    con=Contact.objects.all()
    data={
        'con':con
    }
    return render (req,"contact.html",data)
    