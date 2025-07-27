from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout

# Create your views here.
def register_view(request):
    if (request.method == 'POST'):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # login(request, form.save()) login hen register
            form.save()
            return redirect('posts:list')
    else:
        form = UserCreationForm()
        
    return render(request, 'users/register.html', {'form': form})

def login_view (request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if (form.is_valid()):
            # Login here
            login(request, form.get_user())
            if "next" in request.POST:
                return redirect(request.POST.get("next"))
            else:
                # Redirect to posts list after login
                return redirect('posts:list')
        
        return redirect("users:login")
    else:
        form = AuthenticationForm()

    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('users:login')
    
    return render(request, 'users/logout.html')