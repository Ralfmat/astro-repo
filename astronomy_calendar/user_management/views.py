from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or login page
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'registration.html', {'form': form})

@login_required
def my_protected_view(request):
    # Your view logic here
    return render(request, 'my_protected_template.html')

# views.py

