from django.shortcuts import render, redirect

from items.models import Category, Item
from .forms import SignupForm
# Create your views here.

def index(request):
    items = Item.objects.filter(is_sold=False)
    categories = Category.objects.all()
    print('Items:', items)
    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items
    })


def contact(request):
    return render(request, 'core/contact.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })