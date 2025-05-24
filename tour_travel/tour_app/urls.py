from django.urls import path 
from .views import Home,Menu_page,Booking_page
from django.conf import settings 
from django.conf.urls.static import static 



urlpatterns = [
    path ('',Home, name='Home'),
    path ('Menu',Menu_page, name='Menu'),
    path ('Booking',Booking_page, name='Booking')



]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
