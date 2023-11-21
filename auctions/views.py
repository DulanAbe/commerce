from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django import forms
from django.contrib import messages

from .models import User, Listing

class NewListingForm(forms.Form): 
        title = forms.CharField(label="Title", max_length=100, widget=forms.TextInput(attrs={'class': "form-control"}))
        description = forms.CharField(label="Description", max_length=300, widget=forms.Textarea(attrs={'class':'form-control'}))
        starting_bid = forms.CharField(label="Starting Bid", widget=forms.NumberInput(attrs={'class':'form-control'}))
        url = forms.CharField(label="Image URL (Optional", required=False, widget=forms.URLInput(attrs={'class':"form-control"}))
        CATEGORIES = (
            ('Fashion', 'Fashion'),
            ('Toys', 'Toys'),
            ('Electronics', 'Electronics'),
            ('Home', 'Home'), 
        )
        category = forms.ChoiceField(label="Category (Optional)", required=False, widget=forms.Select(attrs={'class': 'custom-select'}), choices = CATEGORIES)


def index(request):
    # Pass in and loop over all of the listings:
    return render(request, "auctions/index.html", {
        "listings": Listing.objects.all()
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def test(request):
    return render(request, "auctions/image.html")

def listing(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    return render(request, "auctions/listing.html", {
        "listing": listing
    })


def watchlist(request): 
    return render(request, "auctions/watchlist.html")


def new(request):
    if request.method == "POST":
        # Collect and process data from the form:
        form = NewListingForm(request.POST)
        if not form.is_valid():
            return render(request, "auctions/new.html", {
                "form": form
            })
        
        # If the form is valid:
        else: 
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            starting_bid = form.cleaned_data["starting_bid"]
            url = form.cleaned_data["url"]
            category = form.cleaned_data["category"]

            # Create a new row in the database and save it
            new_listing = Listing(
                title = title,
                description = description,
                starting_bid = starting_bid,
                url = url,
                category = category,
            )
            new_listing.save()
            messages.success(request, "Listing Added")
            return redirect(reverse('index'))

    else:    
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        return render(request, "auctions/new.html", {
            "form": NewListingForm()
        })
