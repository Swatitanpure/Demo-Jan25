from django.shortcuts import render, redirect
from .forms import ProductForm

# Create your views here.
def home(request):
    context = {
    'name':'swati',
    'age':25,
    'skills':['python','sql','git','django']
    }

    return render(request,'home.html',context)

def add_product(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form = ProductForm()
        
    return render(request, 'myapp/add_product.html',{'form':form})

