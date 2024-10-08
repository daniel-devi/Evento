from django.contrib import admin
from .models import *

# Register your models here.
class EventAdmin(admin.ModelAdmin):
    # Define which fields to display in the admin list view for Event model
    list_display = ('title', 'date', 'location', 'organizer', 'description')

admin.site.register(Event, EventAdmin)

class TicketAdmin(admin.ModelAdmin):
    # Define which fields to display in the admin list view for Ticket model
    list_display = ('event', 'ticket_type', )

admin.site.register(Ticket, TicketAdmin)

class TicketTypeAdmin(admin.ModelAdmin):
    # Define which fields to display in the admin list view for TicketType model
    list_display = ('name', 'price', 'description')

admin.site.register(TicketType, TicketTypeAdmin)


class UserTicketAdmin(admin.ModelAdmin):
    # Define which fields to display in the admin list view for UserTicket model
    list_display = ('user', 'ticket', 'quantity')

admin.site.register(UserTicket, UserTicketAdmin)


class PaymentAdmin(admin.ModelAdmin):
    # Define which fields to display in the admin list view for Payment model
    list_display = ('user', 'payment_method', 'payment_date', 'payment_status')

admin.site.register(Payment, PaymentAdmin)

class OrderAdmin(admin.ModelAdmin):
    # Define which fields to display in the admin list view for Order model
    list_display = ('user', 'created_at', 'updated_at')

admin.site.register(Order, OrderAdmin)
