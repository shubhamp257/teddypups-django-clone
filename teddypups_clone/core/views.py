from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Puppy, Enquiry

DEMO_PUPPIES = [
 {'name':'Milo','breed':'Toy Poodle','age':'10 weeks','gender':'Male','image_url':'https://images.unsplash.com/photo-1516734212186-a967f81ad0d7?w=900&q=85','description':'A tiny bundle of joy with a gentle, playful personality.'},
 {'name':'Cindy','breed':'Siberian Husky','age':'10 months','gender':'Female','image_url':'https://images.unsplash.com/photo-1550973078-ce53733d6117?q=80&w=685&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=NHwxMjA3fDA%3D','description':'Cindy is a playful, social young Husky based in Chatsworth, California, ready for a loving home that enjoys outdoor adventures.'},
 {'name':'Acorn','breed':'Goldendoodle','age':'3 months','gender':'Female','image_url':'https://images.unsplash.com/photo-1545573139-feec87d23486?q=80&w=687&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=NHwxMjA3fDA%3D','description':'Acorn is a sweet, fluffy young puppy located in San Pedro, California, looking for an affectionate home ready for puppy training and playtime.'},
]
def puppy_data():
    try:
        records = list(Puppy.objects.filter(available=True).values('name','breed','age','gender','image_url','description'))
        return records or DEMO_PUPPIES
    except Exception:
        return DEMO_PUPPIES

def home(request):
    return render(request, 'core/home.html', {'puppies':puppy_data()[:3]})
def puppies(request):
    return render(request, 'core/puppies.html', {'puppies':puppy_data()})
def how_it_works(request):
    return render(request, 'core/how.html')
def families(request):
    return render(request, 'core/families.html')
def faq(request):
    return render(request, 'core/faq.html')
def contact(request):
    return render(request, 'core/contact.html')
def enquiry(request):
    if request.method == 'POST':
        name=request.POST.get('name','').strip()
        email=request.POST.get('email','').strip()
        phone=request.POST.get('phone','').strip()
        message=request.POST.get('message','').strip()
        interest=request.POST.get('interest','').strip()
        if name and email and phone and message:
            try:
                Enquiry.objects.create(name=name,email=email,phone=phone,message=message,interest=interest)
                messages.success(request, 'Thank you! Your enquiry has been received.')
            except Exception:
                messages.success(request, 'Thank you! Please contact us on WhatsApp to complete your enquiry.')
            return redirect('contact')
        messages.error(request, 'Please complete all required fields.')
        return redirect('contact')
    return redirect('contact')
