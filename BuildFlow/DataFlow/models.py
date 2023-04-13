from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    job_number = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=32, null=True, blank=True)
    description = models.CharField(max_length=256, blank=True, null=True)
    project_data = models.ForeignKey('Data', on_delete=models.DO_NOTHING, null=True)
    project_address = models.ForeignKey('Address', on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return str(f"Job Number: {self.job_number}")

class Address(models.Model):
    project_key = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=32, blank=True, null=True)
    number = models.IntegerField(null=True, blank=True)
    street = models.CharField(max_length=16, blank=True, null=True)
    town = models.CharField(max_length=32, blank=True, null=True)
    postcode = models.CharField(max_length=16, blank=True, null=True)

    def __str__(self):
        return str(f"Project Name: {self.name}")

class Data(models.Model):
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    pdf_file = models.FileField(upload_to='pdfs/')
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return str(f"Project: {self.address}")