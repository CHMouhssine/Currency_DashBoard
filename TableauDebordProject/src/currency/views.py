from django.shortcuts import render,redirect
# Create your views here.
import api

def redirect_index(requests):
    return redirect("home",days_range=30,currencies="USD")

def index(requests,days_range=30,currencies="USD"):
    days,rates=api.get_rates(currencies=currencies.split(","),days=days_range)
    time={7:"Week",30:"Month",365:"Year"}.get(days_range,"Personnalisé")
    return render(requests,"app/index.html",context={"days":days,"rates":rates,"time":time,"currencies_str":currencies})