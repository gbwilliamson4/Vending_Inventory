from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *


# Create your views here.


def index(request):
    # items = Item.objects.all()
    items = Item.objects.order_by('name')

    for item in items:
        item.price_per = round(calculate_price_per(item.total_price, item.quantity), 2)
        item.margin_50 = round(calculate_margin(.50, item.price_per), 2) * 100
        item.margin_65 = round(calculate_margin(.65, item.price_per), 2) * 100
        item.margin_75 = round(calculate_margin(.75, item.price_per), 2) * 100
        item.margin_85 = round(calculate_margin(.85, item.price_per), 2) * 100
        item.margin_100 = round(calculate_margin(1, item.price_per), 2) * 100

        # print(item.price_per)
        # print(item.margin_100)

    if request.method != 'POST':
        form = Item_Form()
    else:
        form = Item_Form(request.POST)
        try:
            if form.is_valid():
                form.save()
                return redirect('index')
        except ValueError:
            print("there was an error.")

    context = {'items': items, 'form': form}
    return render(request, 'inventories/index.html', context)

# def index(request):
#     return HttpResponse("Hello. This is the index page.")
def calculate_price_per(total_price, price_per):
    return total_price/price_per


def calculate_margin(markup, price_per):
    # (new_num - old_num)/old_num
    markup = float(markup)
    price_per = float(price_per)
    percentage_change = (markup - price_per)/price_per
    # print("percentage change is:", percentage_change)
    return percentage_change


# Lets create a table to show markups in cents/per container
# another table to show percentage increases
# populate the table
# do some styling
# upload to heroku before Friday.