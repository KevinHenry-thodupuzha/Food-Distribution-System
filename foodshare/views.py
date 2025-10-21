from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import IntegrityError
from .models import FoodPost, Interest
from .forms import RegisterForm, FoodPostForm, InterestForm

def public_feed(request):
    """Public feed showing all food posts"""
    posts = FoodPost.objects.all()
    return render(request, 'foodshare/public_feed.html', {'posts': posts})

@login_required
def user_feed(request):
    """User dashboard showing only their posts"""
    posts = FoodPost.objects.filter(user=request.user)
    return render(request, 'foodshare/user_feed.html', {'posts': posts})

@login_required
def add_post(request):
    """Create a new food post"""
    if request.method == 'POST':
        form = FoodPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            messages.success(request, 'Food post added successfully!')
            return redirect('user_feed')
    else:
        form = FoodPostForm()
    return render(request, 'foodshare/add_post.html', {'form': form})

@login_required
def edit_post(request, pk):
    """Edit an existing food post"""
    post = get_object_or_404(FoodPost, pk=pk, user=request.user)
    if request.method == 'POST':
        form = FoodPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Food post updated successfully!')
            return redirect('user_feed')
    else:
        form = FoodPostForm(instance=post)
    return render(request, 'foodshare/edit_post.html', {'form': form, 'post': post})

@login_required
def delete_post(request, pk):
    """Delete a food post"""
    post = get_object_or_404(FoodPost, pk=pk, user=request.user)
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Food post deleted successfully!')
        return redirect('user_feed')
    return render(request, 'foodshare/delete_post.html', {'post': post})

def register(request):
    """User registration"""
    if request.user.is_authenticated:
        return redirect('public_feed')
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful! Welcome to Surplus Food Saver.')
            return redirect('public_feed')
    else:
        form = RegisterForm()
    return render(request, 'foodshare/register.html', {'form': form})

def user_login(request):
    """User login"""
    if request.user.is_authenticated:
        return redirect('public_feed')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            return redirect('public_feed')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'foodshare/login.html')

@login_required
def user_logout(request):
    """User logout"""
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('public_feed')

@login_required
def post_detail(request, pk):
    """View details of a food post and express interest"""
    post = get_object_or_404(FoodPost, pk=pk)
    user_has_interest = Interest.objects.filter(user=request.user, food_post=post).exists()
    interests = post.interests.all() if post.user == request.user else None
    
    if request.method == 'POST':
        if post.user == request.user:
            messages.error(request, 'You cannot express interest in your own post.')
            return redirect('post_detail', pk=pk)
        
        form = InterestForm(request.POST)
        if form.is_valid():
            try:
                interest = form.save(commit=False)
                interest.user = request.user
                interest.food_post = post
                interest.save()
                messages.success(request, 'Your interest has been registered! The donor will contact you.')
                return redirect('post_detail', pk=pk)
            except IntegrityError:
                messages.error(request, 'You have already expressed interest in this post.')
                return redirect('post_detail', pk=pk)
    else:
        form = InterestForm()
    
    context = {
        'post': post,
        'form': form,
        'user_has_interest': user_has_interest,
        'interests': interests,
        'is_owner': post.user == request.user
    }
    return render(request, 'foodshare/post_detail.html', context)

@login_required
def my_interests(request):
    """View all interests expressed by the user"""
    interests = Interest.objects.filter(user=request.user)
    return render(request, 'foodshare/my_interests.html', {'interests': interests})
