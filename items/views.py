from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.contrib.auth.decorators import login_required
# Create your views here.
from .forms import NewItemForm
def detail(request, pk):
    items = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=items.category, is_sold=False).exclude(pk=pk)[0:3]

    return render(request, 'items/detail.html', {
        'items': items,
        'related_items': related_items
    })
@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect('items:detail', pk=item.id)
    form = NewItemForm()

    return render(request, 'items/form.html', {
        'title': 'New Item',
        'form': form
    })
