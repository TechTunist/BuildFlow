from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    context = {
        'title': 'PJArchitecture',
        'images': ['image1.jpg', 'image2.jpg', 'image3.jpg'],  # Replace this with actual images from the database
        'links': ['Drawings', 'Photos', 'PDFs', 'Other'],  # Replace this with actual links to the different model fields
    }
    return render(request, 'dataflow/home.html', context)
