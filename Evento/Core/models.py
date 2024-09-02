from django.db import models
from django.contrib.auth.models import User
from location_field.models.plain import PlainLocationField
import uuid

# Define event types as choices for the Event model
EventType = [
    ('Workshop', 'Workshop'),
    ('Conference', 'Conference'),
    ('Seminar', 'Seminar'),
    ('Training', 'Training'),
    ('Concert', 'Concert'),
]

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    # Use PlainLocationField for storing geographical coordinates
    location = PlainLocationField(based_fields=['city'], zoom=7, default='40.7128,-74.0060')
    category = models.CharField(max_length=100, choices=EventType)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class TicketType(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='ticket_types')
    name = models.CharField(max_length=100)  # e.g., General, VIP
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    # Optional fields for dynamic pricing
    early_bird_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    last_minute_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    available_from = models.DateTimeField(null=True, blank=True)
    available_until = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.name} - {self.event.title}'

class Ticket(models.Model):
    # Use UUID for unique ticket identification
    ticket_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    ticket_type = models.ForeignKey(TicketType, on_delete=models.CASCADE, related_name='tickets')
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    is_used = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.ticket_type.name} - {self.event.title} - {self.ticket_id}'

class UserTicket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='user_tickets')
    purchase_date = models.DateTimeField(auto_now_add=True)
    is_transferred = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} - {self.ticket.ticket_id}'

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    # Use choices for payment status to ensure data consistency
    payment_status = models.CharField(
        max_length=50,
        choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Failed', 'Failed')],
        default='Pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Order {self.id} - {self.user.username} - {self.event.title}'

# Define payment types as choices for the Payment model
PAYMENTTYPE = [
    ('Credit Card', 'Credit Card'),
    ('PayPal', 'PayPal'),
    ('Stripe', 'Stripe'),
]

class Payment(models.Model):
    # Use OneToOneField to ensure one payment per order
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=50, choices=PAYMENTTYPE)
    payment_date = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=100)

    def __str__(self):
        return f'Payment {self.transaction_id} - {self.order.id}'