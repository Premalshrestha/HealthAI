from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
import re
from .models import UserProfile
# Create your views here.


def is_valid_password(password):
    return (
        len(password) >= 8 and
        re.search(r'[A-Za-z]', password) and
        re.search(r'\d', password)
    )

def landing_page(request):
    return render(request, 'landing_page.html')

def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not email or not password:
            return render(request, 'login.html', {'error': 'Email and password are required.'})

        try:
            user = User.objects.get(username=email)
            if user.check_password(password):
                # Login successful
                return redirect('dashboard')
            else:
                return render(request, 'login.html', {'error': 'Invalid password.'})
        except User.DoesNotExist:
            return render(request, 'login.html', {'error': 'User does not exist.'})
    return render(request, 'login.html')


def is_valid_password(password):
    return (
        len(password) >= 8 and
        re.search(r'[A-Za-z]', password) and
        re.search(r'\d', password)
    )

def user_signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirmation = request.POST.get('passwordConfirmation')
        phone = request.POST.get('phone')
        date_of_birth_str = request.POST.get('dateOfBirth')

        if password != password_confirmation:
            return render(request, 'signup.html', {'error': 'Passwords do not match.'})

        if User.objects.filter(username=email).exists():
            return render(request, 'signup.html', {'error': 'User already exists with this email.'})

        # Create User
        user = User.objects.create_user(
            username=email,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
        )

        profile, created = UserProfile.objects.get_or_create(
            user=user,
            defaults={
                'Phone': phone,
                'Date of Birth': datetime.strptime(date_of_birth_str, '%Y-%m-%d') if date_of_birth_str else None
            }
        )

        return redirect('login')

    return render(request, 'signup.html')


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def diagnosis(request):
    return render(request, 'diagnosis.html')

@login_required
def family(request):
    return render(request, 'family.html')

@login_required
def doctors(request):   
    return render(request, 'doctors.html')
@login_required
def profile(request):   
    user_profile = UserProfile.objects.get(user=request.user)
    return render(request, 'profile.html', {'profile': user_profile})           

def user_logout(request):
    
    logout(request)
    return redirect('landing_page')

