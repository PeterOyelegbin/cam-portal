from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views import generic
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy


# Create your views here.
def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    post_list = Post.objects.filter(title__icontains=q).order_by('-created_on')
    context = {'post_list': post_list}
    return render(request, 'home.html', context)


def registerPage(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = User.objects.create(first_name=firstname, last_name=lastname, username=username, email=email)
            user.set_password(password)
            user.save()
            user_auth = authenticate(username=username, password=password)
            login(request, user_auth)
            return redirect('home')
        except:
            messages.error(request, 'User already exist!')
    return render(request, 'login_register.html')


def loginPage(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Username or password is incorrect!')
        except:
            messages.error(request, 'User does not exist!')       
    return render(request, 'login_register.html', {'page': page})


def logoutUser(request):
    logout(request)
    return redirect('home')


class AddPost(generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'details.html'


class UpdatePost(generic.UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'update_post.html'


class DeletePost(generic.DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


class About(generic.TemplateView):
    template_name = 'about.html'
