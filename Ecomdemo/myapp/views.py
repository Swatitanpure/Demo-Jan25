from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
    'name':'swati',
    'age':25,
    'skills':['python','sql','git','django']
    }

    return render(request,'home.html',context)

