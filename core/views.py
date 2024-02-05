from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from core.models import CustomUser
from internship.models import Item
from django.contrib.auth.decorators import login_required


# Create your views here.


# Rendering the index page and the data displayed 
def index(request):
    return render(request,'index.html')

# Signup View with custom user + django authenticataion system

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.category = form.cleaned_data['category']
            user.save()
            # Your logic for successful registration
            return redirect('login')
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})

#Classic login view
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('browse')  # Replace 'dashboard' with the name or URL pattern of your dashboard view

        else:
            # Handle unsuccessful login
            return render(request, 'registration/login.html', {'error_message': 'Invalid Password or Username'})

    return render(request, 'registration/login.html')

from django.contrib.auth import logout

#Simple Logout View 
def logout_view(request):
    logout(request)
    # Redirect to a success page.
    # return render(request, 'index.html')
    return redirect('home')

#Adding the profile view + personal data to display 
@login_required
def profile(request):
    user=CustomUser()
    items=Item.objects.filter(created_by=request.user)
    return render(request,'profile.html',{
        'user':user,
        'items':items,
    })    

#Simple display of recruiters and candidates views / Future plans add recommendation algorithme here !
def recruiters(request):
    users=CustomUser.objects.filter(category='entreprise')
    return render(request,'accounts/recruiters.html',{
        'users':users,
    })  

def candidates(request):
    users=CustomUser.objects.filter(category='student')
    return render(request,'accounts/candidates.html',{
        'users':users,
    })  