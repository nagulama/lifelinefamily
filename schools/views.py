from django.shortcuts import render
from .models import Post
from django.utils import timezone

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'schools/post_list.html', {'posts':posts})

def Elearning(request):
    return render(request,'schools/Elearning.html')

def Seniorone(request):
    return render(request, 'schools/Seniorone.html')

def Seniortwo(request):
    return render(request, 'schools/Seniortwo.html')
    
def Seniorthree(request):
    return render(request, 'schools/Seniorthree.html')

def Seniorfour(request):
    return render(request, 'schools/Seniorfour.html')

def Seniorfive(request):
    return render(request, 'schools/Seniorfive.html')
    
def Seniorsix(request):
    return render(request, 'schools/Seniorsix.html')