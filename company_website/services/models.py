from django.db import models

# Create your models here.
from django.db import models

from django.db import models

class Review(models.Model):
    name = models.CharField(max_length=255)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.name}"


# Model for general site images like logos, banners, etc.
CATEGORY_CHOICES = [
    ('Graphics Design', 'Graphics Design'),
    ('Construction', 'Construction'),
    ('Cyber Services', 'Cyber Services'),
    ('Entertainment', 'Entertainment'),
]

class ServiceCategory(models.Model):
    name = models.CharField(max_length=100, choices=CATEGORY_CHOICES, unique=True)

    def __str__(self):
        return self.name

class Service(models.Model):
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='service_images/')  # Add image field here

    def __str__(self):
        return self.name

class SiteImage(models.Model):
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='site_images/')
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.category.name} - {self.description}"


class ContactInfo(models.Model):
    email = models.EmailField(default="samamwa13@gmail.com")
    phone = models.CharField(max_length=15, default="+254715825808")
    whatsapp = models.CharField(max_length=15, default="+254715825808")

    def __str__(self):
        return self.email

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"