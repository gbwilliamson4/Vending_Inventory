from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
import math
from django.db.models import Sum


# Create your views here.


def index(request):
    # items = Item.objects.all()
    items = Item.objects.order_by('name')

    for item in items:
        item.price_per = round(calculate_price_per(item.total_price, item.quantity), 2)
        item.margin_50 = math.trunc(calculate_margin(.50, item.price_per) * 100)
        item.margin_65 = math.trunc(calculate_margin(.65, item.price_per) * 100)
        item.margin_75 = math.trunc(calculate_margin(.75, item.price_per) * 100)
        item.margin_85 = math.trunc(calculate_margin(.85, item.price_per) * 100)
        item.margin_100 = math.trunc(calculate_margin(1, item.price_per) * 100)
        # print(math.trunc(item.margin_75))
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
    return render(request, 'Inventories/index.html', context)


# def index(request):
#     return HttpResponse("Hello. This is the index page.")
def calculate_price_per(total_price, price_per):
    return total_price / price_per


def calculate_margin(markup, price_per):
    # (new_num - old_num)/old_num
    markup = float(markup)
    price_per = float(price_per)
    percentage_change = (markup - price_per) / price_per
    # print("percentage change is:", percentage_change)
    return percentage_change


def needed_inventory(request):
    needed_inventory_items = Needed_Inventory.objects.filter(purchased=False)
    purchased_items = Needed_Inventory.objects.filter(purchased=True)  # These will be things that I need to pay on.
    # Once the purchased items have been paid on, I'll admin_approve them to cause them to be deleted from the table
    # and moved to a purchase history table fro record keeping.
    money_owed = calculate_money_owed(purchased_items)

    if request.method != 'POST':
        form = Needed_Inventory_Form()
    else:
        form = Needed_Inventory_Form(request.POST)
        try:
            if form.is_valid():
                form.save()
                return redirect('needed_inventory')
        except ValueError:
            print("there was an error.")

    context = {'needed_inventory_items': needed_inventory_items, 'purchased_items': purchased_items,
               'money_owed': money_owed, 'form': form}
    return render(request, 'Inventories/needed_inventory.html', context)


def to_buy(request):
    needed_inventory_items = Needed_Inventory.objects.filter(purchased=False)
    pending_items = Needed_Inventory.objects.filter(purchased=True)
    purchased_items = Needed_Inventory.objects.filter(purchased=True)
    money_owed = calculate_money_owed(purchased_items)

    context = {'needed_inventory_items': needed_inventory_items, 'purchased_items': purchased_items,
               'money_owed': money_owed}

    return render(request, 'Inventories/to_buy.html', context)


def calculate_money_owed(queryset):
    money_owed = 0
    for item in queryset:
        money_owed += item.item.total_price

    return money_owed/2


def purchased(request, pk):
    return HttpResponse(f"Hello. This is the index page. Primary key is: {pk}")