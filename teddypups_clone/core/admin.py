from django.contrib import admin
from .models import Puppy, Enquiry

@admin.register(Puppy)
class PuppyAdmin(admin.ModelAdmin):
    list_display = ('name','breed','age','gender','available')
    list_filter = ('breed','available')
    search_fields = ('name','breed')
    
@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('name','email','phone','created_at')
    search_fields = ('name','email','phone')
