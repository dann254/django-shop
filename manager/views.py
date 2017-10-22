# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import Http404
from .forms import PurchaseForm
from .models import Stock, Purchase, Sell, Purge

# Create your views here.
def addstock(request):
    errors=None
    success=None
    if request.method == "POST":
        try:
            int(request.POST.get('quantity'))
            if int(request.POST.get('quantity')) <= 0:
                return render(request, "add.html", {"errors": "Quantity must be greater than 0"})
        except:
            return render(request, "add.html", {"errors": "Please enter a valid quantity"})
        try:
            if request.POST.get('name').strip() == "":
                return render(request, "add.html", {"errors": "please enter a valid name", "success":success})
            item = Stock.objects.get(name=request.POST.get('name').lower())
            if item:
                item.quantity = item.quantity + int(request.POST.get('quantity'))
                item.save()
                obj2 = Purchase.objects.create(
                    name = request.POST.get('name').lower(),
                    price = item.price,
                    quantity = request.POST.get('quantity'),
                )

                success="Successfully updated"
                return render(request, "add.html", {"errors": errors, "success":success})
        except:
            try:
                int(request.POST.get('price'))
                if int(request.POST.get('price')) <= 0:
                    return render(request, "add.html", {"errors": "Price must be greater than 0"})
            except:
                return render(request, "add.html", {"errors": "Please enter a valid price"})
            obj = Stock.objects.create(
                name = request.POST.get('name').lower(),
                price = request.POST.get('price'),
                quantity = request.POST.get('quantity'),
            )
            obj2 = Purchase.objects.create(
                name = request.POST.get('name').lower(),
                price = request.POST.get('price'),
                quantity = request.POST.get('quantity'),
            )
            success="Successfully added"
    return render(request, "add.html", {"errors": errors, "success":success})

def sell(request):
    errors=None
    success=None
    if request.method == "POST":
        try:
            int(request.POST.get('quantity'))
            if int(request.POST.get('quantity')) <= 0:
                return render(request, "sell.html", {"errors": "Quantity must be greater than 0"})
        except:
            return render(request, "sell.html", {"errors": "Please enter a valid quantity"})
        try:
            item = Stock.objects.get(name=request.POST.get('name').lower())
            if item:
                if item.quantity < int(request.POST.get('quantity')):
                    return render(request, "sell.html", {"errors": "you do not have enough items in stock"})
                item.quantity = item.quantity - int(request.POST.get('quantity'))
                item.save()
                obj2 = Sell.objects.create(
                    name = request.POST.get('name').lower(),
                    price = item.price,
                    quantity = request.POST.get('quantity'),
                )
                success="Sold"
        except:
            errors="You dont have an item with that name"
    return render(request, "sell.html", {"errors": errors, "success":success})

def stock(request):
    msg = None
    obj = Stock.objects.all()
    if not obj.count():
        msg = "No items yet"
    return render(request, "stock.html", {"obj": obj, "msg":msg})

def item(request, id):
    try:
        item = Stock.objects.get(pk=id)
    except:
        raise Http404
    return render(request, "item.html", {"item":item})

def Update(request, id):
    errors=None
    success=None
    old=None
    try:
        old = Stock.objects.get(id=id)

        if request.method == "POST":
            try:
                int(request.POST.get('price'))
                if int(request.POST.get('price')) <= 0:
                    return render(request, "update.html", {"errors": "price must be greater than 0"})
            except:
                return render(request, "update.html", {"errors": "Please enter a valid price"})
            try:
                if old:
                    item = old
                    item.price = int(request.POST.get('price'))
                    item.save()
                    success="Updated"
            except:
                errors="Item does not exist"
    except:
        error = "Item does not exists"
    return render(request, "update.html", {"errors": errors, "success":success, "item":old})


def Reports(request):
    pr = Purchase.objects.all()
    sl = Sell.objects.all()
    pg = Purge.objects.all()
    return render(request, "report.html", {"pr":pr, "sl":sl, "pg":pg})
def Delete(request, id):
    try:
        item = Stock.objects.get(id=id)
        obj = Purge.objects.create(
            name = item.name,
            price = item.price,
            quantity = item.quantity,
        )
        Stock.objects.filter(id=id).delete()
        obj = Stock.objects.all()
        msg = "Item deleted"
    except:

        obj = Stock.objects.all()
        msg = "Item does not exists"

    return render(request, "stock.html", {"obj": obj, "msg":msg})
