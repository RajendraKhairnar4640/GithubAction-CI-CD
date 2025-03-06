from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test

# Check if user is superuser
def superuser_required(user):
    return user.is_superuser

# Custom login view
def custom_login(request):
    if request.user.is_authenticated:
        return redirect('admin_dashboard')  # Redirect logged-in users to dashboard
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user and user.is_superuser:
            login(request, user)
            return redirect('admin_dashboard')
        else:
            return render(request, 'admin_panel/login.html', {'error': 'Invalid credentials or not a superuser'})
    
    return render(request, 'login.html')

# Logout view
def custom_logout(request):
    logout(request)
    return redirect('custom_login')  # Redirect to login page after logout

# Protected dashboard (only for superusers)
@login_required
@user_passes_test(superuser_required)
def dashboard(request):
    return render(request, 'dashboard.html')
