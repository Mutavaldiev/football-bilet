
from django.contrib import admin
from .models import *

@admin.register(Games)
class GamesAdmin(admin.ModelAdmin):
    list_display = ('team_home','team_away','category','stadium','date','ticket_price','is_active')
    list_filter = ('category', 'is_active', 'date')
    search_fields = ('team_home__name', 'team_away__name')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','user','game','quantity','total_price','created_at')



admin.site.register(Team)
admin.site.register(Category_tip_sport)
admin.site.register(Ticket)
admin.site.register(Profile)
