from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    return render(request, 'index.html')

def generate_blog(request):
   pass 

def user_login(request):
    error_message = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            error_message = "Invalid username or password"
    
    # Pass error_message to the context when rendering the template
    return render(request, 'login.html', {'error_message': error_message})

def user_signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeatPassword')  # Changed to match the input name
        
        if password == repeat_password:
            try:
                # Check if username or email already exists
                if User.objects.filter(username=username).exists():
                    error_message = 'Username already exists'
                elif User.objects.filter(email=email).exists():
                    error_message = 'Email already exists'
                else:
                    # Create user
                    user = User.objects.create_user(username=username, email=email, password=password)
                    user.save()
                    login(request, user)
                    return redirect('/')
            except Exception as e:
                error_message = f'Error creating account: {str(e)}'
        else:
            error_message = 'Passwords do not match'
        
        return render(request, 'signup.html', {'error_message': error_message})
    return render(request, 'signup.html')

def user_logout(request):
    pass