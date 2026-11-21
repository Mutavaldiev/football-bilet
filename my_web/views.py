from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
from .models import *


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})




def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})





def logout_view(request):
    if request.method == 'POST':
        logout(request)
    return redirect('home')





@login_required
def profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        if request.FILES.get('image'):
            profile.image = request.FILES['image']
            profile.save()
            messages.success(request, 'Profile updated!')
    return render(request, 'profile.html', {'profile': profile})




def home(request):
    games = Games.objects.filter(is_active=True)
    categories = Category_tip_sport.objects.all()
    search = request.GET.get('search') or request.GET.get('q')
    category = request.GET.get('category')
    if search:
        games = games.filter(
            Q(team_home__name__icontains=search) | Q(team_away__name__icontains=search) |
            Q(stadium__icontains=search) | Q(city__icontains=search))
    if category:
        games = games.filter(category_id=category)
    return render(request, 'home.html', {'games': games,'categories': categories})





def game_detail(request, id):
    game = get_object_or_404( Games, id=id, is_active=True)
    return render(request, 'game_detail.html', { 'game': game})











@login_required
def my_tickets(request):
    orders = Order.objects.filter(ser=request.user
    ).select_related('game','game__team_home','game__team_away'
    ).prefetch_related('tickets'
    ).order_by('-created_at')
    return render(request, 'my_tickets.html', {'orders': orders})


@login_required
def cancel_ticket(request, id):
    order = get_object_or_404(Order,id=id,user=request.user)
    if request.method == 'POST':
        order.delete()
        messages.success(request, 'Билет бекор карда шуд!')
    return redirect('my_tickets')
