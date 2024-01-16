from django.shortcuts import render, get_object_or_404
from .models import *
# Create your views here.
def detail(request, pk):
    items = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=items.category, is_sold=False).exclude(pk=pk)[0:3]

    return render(request, 'items/detail.html', {
        'items': items,
        'related_items': related_items
    })