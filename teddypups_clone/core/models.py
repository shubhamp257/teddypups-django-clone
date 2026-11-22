from django.db import models
class Puppy(models.Model):
    name = models.CharField(max_length=80)
    breed = models.CharField(max_length=80)
    age = models.CharField(max_length=40, blank=True)
    gender = models.CharField(max_length=20, blank=True)
    price = models.CharField(max_length=40, blank=True)
    description = models.TextField(blank=True)
    image_url = models.URLField()
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Enquiry(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    interest = models.CharField(max_length=120, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.name} - {self.created_at:%Y-%m-%d}'
