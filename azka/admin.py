from django.contrib import admin
from .models import Project,Event,Testimonial,Regisration,Gallery,SchoolInformation
from django.contrib.auth.models import Group	
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display=['id','title','detail'] 

    
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display=['id','image','desc'] 
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display=['id','title','progress','start_date','detail','image',]
@admin.register(SchoolInformation)
class SchoolInformationAdmin(admin.ModelAdmin):
    list_display=['our_students','our_teachers','our_courses','our_rewards']     
           




@admin.register(Regisration)
class RegistrationAdmin(admin.ModelAdmin):   
    list_display=['id','username','father_name','email','phone_no','dob','address','department','is_active']


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display=['id','image']    

# admin.site.register(Regisration)


admin.site.site_header="Azka School"
admin.site.unregister(Group)
