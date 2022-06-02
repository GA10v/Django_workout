from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from .forms import UpdateUserForm, UpdateProfileForm



# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user-login')
    else:
        form = UserCreationForm()
    context = {
        'form' : form
    }

    return render(request, template_name='user/login.html', context=context)


def profile(request):
    return render(request, template_name='user/profile.html')


def profile_update(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('user-profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)
    
    context = {
        'user_form' : user_form,
        'profile_form' : profile_form,
    }


    return render(request, template_name='user/profile_update.html', context=context)