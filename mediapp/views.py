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
def user_dashboard(request):
    print("Dashboard view called")  # Debug log


    user = request.user
    print(user.username)
    print(user.email)
    print(user.first_name)
    print(user.last_name)

    return render(request, 'dashboard.html', {'user': user})

@login_required
def diagnosis(request):
    return render(request, 'diagnosis.html')
from pyexpat.errors import messages
from django.contrib.auth.decorators import login_required
@login_required
def family(request):
    print("Family view called")  # Debug log
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        print(profile.family)
        family = profile.family
        
        members = UserProfile.objects.filter(family=profile.family)
        print("Family members:", members)
    else:
        messages.success(request, 'You Must logged in')
        return redirect('/')

    print(profile)


    return render(request, 'family.html', {'family': family, 'members': members})

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

def ai_diagnosis0(request):
   return render(request, 'AI_diag0.html')

def ai_diagnosis1(request):
   return render(request, 'AI_diag1.html')

def ai_diagnosis2(request):
   return render(request, 'AI_diag2.html')

def ai_diagnosis3(request):
   return render(request, 'AI_diag3.html')

from .models import Family, UserProfile
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import UserProfile

@login_required
def add_family(request):
    if request.method == 'POST':
        username = request.POST.get('username')

        try:
            # Get the user by username
            target_user = User.objects.get(username=username)
            target_profile = UserProfile.objects.get(user=target_user)

            # Current user's profile and family
            current_profile = UserProfile.objects.get(user=request.user)

            if not current_profile.family:
                return render(request, 'add_family.html', {
                    'error': 'You are not associated with any family. Please create a family first.'
                })

            # Assign the found user to the same family
            target_profile.family = current_profile.family
            target_profile.save()

            return render(request, 'add_family.html', {
                'success': f'User "{target_user.username}" added to your family successfully.'
            })

        except User.DoesNotExist:
            return render(request, 'add_family.html', {'error': 'User with that username does not exist.'})
        except UserProfile.DoesNotExist:
            return render(request, 'add_family.html', {'error': 'User profile not found.'})

    return render(request, 'add_family.html')



# View to collect the answer from the form and move to the next question
import os
import pickle
from django.shortcuts import render
from .forms import HeartPredictionForm
from django.conf import settings
model = None

def load_model():
    global model
    if model is None:
        model_path = os.path.join(settings.BASE_DIR, 'mediapp', 'model', 'framingham_model.pkl')
        with open(model_path, 'rb') as f:
            model = pickle.load(f)

load_model()

def predict_heart_disease(request):
    prediction = None
    probability = None

    if request.method == 'POST':
        form = HeartPredictionForm(request.POST)
        if form.is_valid():
            data = [
                int(form.cleaned_data['male']),
                form.cleaned_data['age'],
                int(form.cleaned_data['currentSmoker']),
                form.cleaned_data['cigsPerDay'],
                int(form.cleaned_data['BPMeds']),
                int(form.cleaned_data['prevalentStroke']),
                int(form.cleaned_data['prevalentHyp']),
                int(form.cleaned_data['diabetes']),
                form.cleaned_data['totChol'],
                form.cleaned_data['sysBP'],
                form.cleaned_data['diaBP'],
                form.cleaned_data['BMI'],
                form.cleaned_data['heartRate'],
                form.cleaned_data['glucose'],
                int(form.cleaned_data['cholesterolLevel']),
                int(form.cleaned_data['obesity']),
                int(form.cleaned_data['bloodPressureLevel']),
                int(form.cleaned_data['heartRateLevel']),
                int(form.cleaned_data['diabetesLevel']),
                int(form.cleaned_data['chestPain_1']),
                int(form.cleaned_data['shortnessOfBreath_yes']),
                int(form.cleaned_data['dizziness_yes']),
                int(form.cleaned_data['hereditaryDisease_yes']),
            ]

            prediction = model.predict([data])[0]
            probability = model.predict_proba([data])[0][1] * 100

    else:
        form = HeartPredictionForm()

    return render(request, 'prediction_form.html', {
        'form': form,
        'prediction': prediction,
        'probability': round(probability, 2) if probability is not None else None,
        })