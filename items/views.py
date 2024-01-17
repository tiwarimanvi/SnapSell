from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.contrib.auth.decorators import login_required
# Create your views here.
from .forms import NewItemForm, EditItemForm
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


@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()

    return redirect('dashboard:index')

@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            item.save()

            return redirect('items:detail', pk=item.id)
    form = EditItemForm(instance=item)

    return render(request, 'items/form.html', {
        'title': 'Edit Item',
        'form': form
    })
