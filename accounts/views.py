from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import UserModel
from .forms import UserCreationForm, UserUpdateForm


# Create your views here.
@login_required(login_url='http://127.0.0.1:8000/accounts/login')
def listUsers(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    users = UserModel.objects.filter(first_name__icontains=q)
    return render(request, 'registration/listUsers.html', {'staffs': users})


@login_required(login_url='http://127.0.0.1:8000/accounts/login')
def userDetails(request, pk):
    user = UserModel.objects.get(id=pk)
    return render(request, 'registration/userDetails.html', {'staff': user})


@login_required(login_url='http://127.0.0.1:8000/accounts/login')
def createUser(request):
    formset = UserCreationForm(request.POST or None)
    if formset.is_valid():
        send_mail(
            subject='LAPS: User Created',
            message= f"Dear {formset.data['first_name']} {formset.data['last_name']},\n\nCongratulations! You have successfully been created on the LAPS platform in the ALERT MICROFINANCE BANK LTD Institution, a default password was created for you and can be change to a preferred one by clicking forget password. Please log in with the following default credentials below:\nemail: {formset.data['email']}\npassword: {formset.data['password']}\n\nRegards,\nLAPS Team\n{settings.EMAIL_HOST_USER}\nhttps://laps.vercel.app",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[formset.data['email']]
        )
        formset.save()
        messages.success(request, 'User added successfully')
        return redirect('users')
    else:
        return render(request, 'registration/createUser.html', {'formset': formset})


@login_required(login_url='http://127.0.0.1:8000/accounts/login')
def updateUser(request, pk):
    object = get_object_or_404(UserModel, id=pk)
    formset = UserUpdateForm(request.POST or None, instance=object)
    if formset.is_valid():
        formset.save()
        messages.success(request, 'User data successfully updated')
        return redirect('/accounts/users/'+pk)
    else:
        return render(request, 'registration/updateUser.html', {'formset': formset})


@login_required(login_url='http://127.0.0.1:8000/accounts/login')
def deleteUser(request, pk):
    user = UserModel.objects.get(id=pk)
    user.delete()
    messages.success(request, 'User deleted successfully')
    return redirect('users')


def loginUser(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = authenticate(request, email=email.lower(), password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'email or password is incorrect!')
        except:
            messages.error(request, 'user does not exist!')       
    return render(request, 'registration/login.html')


@login_required(login_url='http://127.0.0.1:8000/accounts/login')
def logoutUser(request):
    logout(request)
    return redirect('home')
