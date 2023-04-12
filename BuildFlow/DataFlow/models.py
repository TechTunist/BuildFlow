from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    client = models.ManyToManyField(User)
    job_number = models.IntegerField(blank=False, null=True)
    description = models.CharField(max_length=256, blank=True, null=True)

class Address(models.Model):
    project = models.ForeignKey(Project,  on_delete=models.CASCADE)
    post_code = models.CharField(max_length=32)
    postal_address = models.CharField(max_length=64, blank=True)

class Data(models.Model):
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    pdf_file = models.FileField(upload_to='pdfs/')
    image = models.ImageField(upload_to='images/')