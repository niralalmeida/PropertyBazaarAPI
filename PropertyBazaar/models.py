from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from rest_framework.authtoken.models import Token


CITIES = [(item, item) for item in ['Pune', 'Mumbai']]
TYPES = [(item, item) for item in ['Bungalow', 'Apartment', 'Villa']]


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Property(models.Model):
    title = models.CharField(max_length=25, null=False)
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=500, blank=True, default='')
    propertytype = models.CharField(choices=TYPES, default='Bungalow', max_length=10)
    address = models.CharField(max_length=100, null=False)
    city = models.CharField(choices=CITIES, default='Mumbai', max_length=10)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='properties')
    bathrooms = models.IntegerField(null=True, default=0)
    bedrooms = models.IntegerField(null=True, default=0)
    garages = models.IntegerField(null=True, default=0)
    rooms = models.IntegerField(null=True, default=0)
    area = models.IntegerField(null=False)
    price = models.IntegerField(null=False)
    image = models.ImageField(upload_to='images/properties/', null=True, default=None)

    def __str__(self):
        return self.title + ' by ' + str(self.owner)

    class Meta:
        ordering = ('created', )
        verbose_name = 'Property'
        verbose_name_plural = 'Properties'
