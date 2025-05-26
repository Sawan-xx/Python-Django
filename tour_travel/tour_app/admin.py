from django.contrib import admin
from .models import destinations , booking ,cars,Contact

# Register your models here.
class destination_Admin(admin.ModelAdmin):
    list_display=['d_name','discription','price','d_img']
    list_editable=['discription','price','d_img']
    

admin.site.register(destinations,destination_Admin)


class booking_Admin(admin.ModelAdmin):
    list_display=['user','destination','booking_date','travel_date']
    list_editable=['destination','travel_date']
    list_display_links=['user']
    

admin.site.register(booking,booking_Admin)

class cars_Admin(admin.ModelAdmin):
    list_display=['car_name','car_colour','description','car_img']


admin.site.register(cars,cars_Admin)



class Contact_admin(admin.ModelAdmin):
    list_display=['Name','Contact','Email']
    
admin.site.register(Contact,Contact_admin)


admin.site.site_title="ShubhamTourAndTravels"
admin.site.site_header="ShubhamTourAndTravels"