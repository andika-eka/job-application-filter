from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Applicant(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    
    email = models.EmailField(max_length=254)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    class Meta:

    # renames the instances of the model
    # with their title name  
        def __str__(self):
            return self.title