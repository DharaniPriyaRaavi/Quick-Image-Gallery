from .models import Item
import os
from django.db.models import Q
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UserRegistrationForm
import datetime
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse


# Create your views here.

def index(request):
    products = Item.objects.all()
    context = {'products': products}
    return render(request, 'products/index.html', context)


def about(request):
    return render(request, 'products/about.html')


def addProduct(request):
    if request.method == "POST":
        prod = Item()
        prod.name = request.POST.get('name')
        prod.description = request.POST.get('description')
        prod.price = request.POST.get('price')

        if len(request.FILES) != 0:
            prod.image = request.FILES['image']

        prod.save()
        messages.success(request, "Product Added Successfully")
        return redirect('/')
    return render(request, 'products/add.html')


def editProduct(request, pk):
    prod = Item.objects.get(id=pk)

    if request.method == "POST":
        if len(request.FILES) != 0:
            if len(prod.image) > 0:
                os.remove(prod.image.path)
            prod.image = request.FILES['image']
        prod.name = request.POST.get('name')
        prod.description = request.POST.get('description')
        prod.slug = request.POST.get('slug')
        prod.tags = request.POST.get('tags')
        prod.price = request.POST.get('price')
        prod.save()
        messages.success(request, "Product Updated Successfully")
        return redirect('/')

    context = {'prod': prod}
    return render(request, 'products/edit.html', context)


def deleteProduct(request, pk):
    prod = Item.objects.get(id=pk)
    if len(prod.image) > 0:
        os.remove(prod.image.path)
    prod.delete()
    messages.success(request, "Product Deleted Successfuly")
    return redirect('/')


def search(request):
    query = None
    result = []
    if request.method == 'GET':
        query = request.GET.get('search')
        result = Item.objects.filter(Q(name__icontains=query) | Q(tags__icontains=query))
    return render(request, 'products/search.html', {'query': query, 'result': result})


def register(response):
    if response.method == "POST":
        form = UserRegistrationForm(response.POST)
        if form.is_valid():
            register = form.save(commit=False)
            register.password = make_password(form.cleaned_data['password1'])
            form.save()
        return render(response, 'products/login.html')
    else:
        form = UserRegistrationForm()
    return render(response, "products/register.html", {"form": form})


# Create your views here.
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        request.session['username'] = username
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                now = datetime.datetime.now()
                request.session['last_login'] = now.strftime('%d-%m-%Y %H:%M:%S')
                request.session.set_expiry(60)
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                else:
                    return HttpResponseRedirect(reverse('/'))
            else:
                return HttpResponse('Your account is disabled.')
        else:
            return HttpResponse('Invalid login details.')
    else:
        return render(request, 'products/login.html')


@login_required(login_url='/login')
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))
