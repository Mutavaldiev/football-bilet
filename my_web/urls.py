from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('game/<int:id>/', views.game_detail, name='game_detail'),
    path('buy/<int:id>/', views.buy_ticket, name='buy_ticket'),
    path('my-tickets/', views.my_tickets, name='my_tickets'),
    path('cancel/<int:id>/', views.cancel_ticket, name='cancel_ticket'),
]
