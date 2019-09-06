from django.shortcuts import render,redirect
from .models import Image,Car,Comments,Category
from django.contrib.auth.decorators import login_required
from .forms import CarForm,CommentForm

# Create your views here.
def welcome(request):
    categories = Category.objects.all()
    images = Image.objects.all()    
    return render(request,'welcome.html',{'images':images,'categories':categories})

def category_filter(request,category_id):
    categories = Category.objects.all()
    images = Image.objects.filter(category=category_id)
    return render(request,'category.html',{'categories':categories,"images":images})


@login_required(login_url='/accounts/login/')
def car(request):
    logged_user = request.user
    images = Image.objects.all()
    if request.method == 'POST':
        form = CarForm(request.POST,request.FILES)
        if form.is_valid():
            edit = form.save(commit=False)
            edit.user = logged_user
            edit.save()
        return redirect('view_car')

    else:

        form = CarForm()

    return render(request,'car.html',{'form':form,'images':images})


@login_required(login_url='/accounts/login/')
def view_car(request):
    cars = Car.objects.all()

    return render(request,'view_car.html',{"cars":cars})



@login_required(login_url='/accounts/login/')
def comment(request):
    logged_user = request.user
    comments = Comments.objects.all()
    if request.method == 'POST':
        form = CommentForm(request.POST,request.FILES)
        if form.is_valid():
            edit = form.save(commit=False)
            edit.user = logged_user
            edit.save()
        return redirect('welcome')

    else:

        form = CommentForm()

    return render(request,'comments.html',{'form':form})




