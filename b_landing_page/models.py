import uuid
from django.db import models
from django.core.validators import RegexValidator

zip_validator = RegexValidator(r'^\d{5}(?:[-\s]\d{4})?$')
#phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")


class CountyCoverage(models.Model):
    county = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    
    def __str__(self):
        return self.county + ' County, '+ self.state
    
    class Meta:
        ordering = ['state', 'county']
        
        
class Distributor(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=10, validators=[zip_validator])
    phone = models.CharField(max_length=17, blank=True)
    email = models.CharField(max_length=200)
    contact_name = models.CharField(max_length=200)
    contact_phone = models.CharField(max_length=17, blank=True)
    contact_email = models.CharField(max_length=200)
    contact_title = models.CharField(max_length=200)
    coverage = models.ManyToManyField(CountyCoverage, blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']