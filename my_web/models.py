from django.db import models
from django.conf import settings


class Category_tip_sport(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name





class Team(models.Model):
    name = models.CharField(max_length=150)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name





class Games(models.Model):
    category = models.ForeignKey(Category_tip_sport,on_delete=models.CASCADE,related_name='games')
    team_home = models.ForeignKey( Team, on_delete=models.CASCADE, related_name='home_games')
    team_away = models.ForeignKey( Team, on_delete=models.CASCADE, related_name='away_games')
    stadium = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    date = models.DateTimeField()
    description = models.TextField(blank=True)
    ticket_price = models.DecimalField(max_digits=10,decimal_places=2)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.team_home} vs {self.team_away}'





class Order(models.Model):
    STATUS_CHOICES = [('pending', 'Pending'),('paid', 'Paid'),('cancelled', 'Cancelled'),]
    user = models.ForeignKey( settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders')
    game = models.ForeignKey( Games, on_delete=models.CASCADE, related_name='orders')
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10,decimal_places=2)
    status = models.CharField( max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order #{self.id}'


class Ticket(models.Model):
    order = models.ForeignKey( Order, on_delete=models.CASCADE, related_name='tickets')
    sector = models.CharField(max_length=50)
    row = models.PositiveIntegerField()
    seat_number = models.PositiveIntegerField()
    price = models.DecimalField( max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.sector} - Row {self.row} - Seat {self.seat_number}'




class Profile(models.Model):
    user = models.OneToOneField( settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(upload_to='profiles/',default='profiles/default.png',blank=True)

    def __str__(self):
        return self.user.username
