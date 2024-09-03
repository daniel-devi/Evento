from django.db import models
from django.contrib.auth.models import User
from django.templatetags.static import static
from location_field.models.plain import PlainLocationField
from django.conf import settings  # Import settings instead of BASE_DIR directly
import uuid
import qrcode
import PIL
import os

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
    location = PlainLocationField(based_fields=['city'], zoom=7, default='-0.1655385435678049,-0.848121657036245')
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
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.ticket_type.name} - {self.event.title} - {self.ticket_id}'

class UserTicket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='user_tickets')
    qrcode = models.ImageField(upload_to='qr_codes/', null=True, blank=True)
    quantity = models.PositiveIntegerField()
    purchase_date = models.DateTimeField(auto_now_add=True)
    is_used = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # Generate QR code if it doesn't exist
        if not self.qrcode:
            self.qrcode = self.generate_qr_code(self)
        super().save(*args, **kwargs)  # Call the "real" save() method
    
    @staticmethod
    def generate_qr_code(instance):
        """
        Generate and save a QR code image for a ticket.
        
        This function creates a QR code with the ticket ID, adds a logo to it,
        and saves the resulting image.
        """
        # Load and resize the logo
        logo_path = static('images/logo.png')
        logo_full_path = os.path.join(settings.BASE_DIR, 'static', logo_path.lstrip('/'))  # Fix the path joining
        LOGO = PIL.Image.open(logo_full_path)
        BASEWIDTH = 100
        
        # Adjust image size while maintaining aspect ratio
        width_percent = (BASEWIDTH / float(LOGO.size[0]))
        height_size = int((float(LOGO.size[1]) * float(width_percent)))
        logo = LOGO.resize((BASEWIDTH, height_size), PIL.Image.LANCZOS) 

        if hasattr(instance, 'ticket'):  # Check if ticket attribute exists
            # Create QR code instance
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            
            # Add ticket ID data to QR code
            qr.add_data(str(instance.ticket.ticket_id))
            qr.make(fit=True)
            
            # Generate QR code image with custom colors
            img = qr.make_image(fill_color="orange", back_color="white")
            
            # Calculate position to center the logo on the QR code
            logo_position = ((img.size[0] - logo.size[0]) // 2, (img.size[1] - logo.size[1]) // 2)
            
            # Paste the logo onto the QR code
            img.paste(logo, logo_position)
            
            # Save the QR code image
            qr_code_path = f'qr_codes/{instance.ticket.ticket_id}.png'
            img.save(os.path.join(settings.MEDIA_ROOT, qr_code_path))  # Use MEDIA_ROOT for saving
            
            # Save the QR code image path to the model field
            instance.qrcode.save(qr_code_path, img)

            return qr_code_path    
        else:
            # Handle the case where the ticket attribute doesn't exist
            return None

    def __str__(self):
        return f'{self.user.username} - {self.ticket.ticket_id}'

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Use OneToOneField to ensure one payment per order
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=50, choices=PAYMENTTYPE)
    # Use choices for payment status to ensure data consistency
    payment_status = models.CharField(
        max_length=50,
        choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Failed', 'Failed')],
        default='Pending'
    )
    payment_date = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=100)

    def __str__(self):
        return f'Payment {self.transaction_id} - {self.order.id}'
