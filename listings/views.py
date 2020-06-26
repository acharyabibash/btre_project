""" This Docstring is used for Views
    Author : Bibash Achara
    Date : 6/26/2019
"""



from django.shortcuts import render

from .models import Listing

def index(request):
    """ Function USed for querying through objects"""
    listings = Listing.objects.all()   
    context = {
        'listings':listings,
    }   
    return render(request,'listings/listings.html')

def listing(request):
    return render(request,'listings/listing.html')

def search(request):
    return render(request,'listings/search.html')

