from django.contrib import admin
from django.urls import path
from core import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('puppies/', views.puppies, name='puppies'),
    path('how-it-works/', views.how_it_works, name='how_it_works'),
    path('happy-families/', views.families, name='families'),
    path('faq/', views.faq, name='faq'),
    path('visit-contact/', views.contact, name='contact'),
    path('enquiry/', views.enquiry, name='enquiry'),
]
