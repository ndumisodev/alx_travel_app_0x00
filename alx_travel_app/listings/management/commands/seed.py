from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from listings.models import Property, Booking, Review, Payment, Message
import uuid
from datetime import datetime, timedelta
import random

User = get_user_model()

class Command(BaseCommand):
    help = 'Seeds the database with sample data'

    def handle(self, *args, **options):
        self.stdout.write('Seeding data...')
        
        # Create users
        host = User.objects.create_user(
            email='host@example.com',
            first_name='John',
            last_name='Host',
            password='testpass123',
            role='host'
        )
        
        guest = User.objects.create_user(
            email='guest@example.com',
            first_name='Jane',
            last_name='Guest',
            password='testpass123',
            role='guest'
        )
        
        admin = User.objects.create_user(
            email='admin@example.com',
            first_name='Admin',
            last_name='User',
            password='testpass123',
            role='admin'
        )
        
        # Create properties
        property1 = Property.objects.create(
            host=host,
            name='Cozy Apartment in Downtown',
            description='Beautiful apartment in the heart of the city',
            location='New York, NY',
            property_type='apartment',
            price_per_night=120.00
        )
        
        property2 = Property.objects.create(
            host=host,
            name='Luxury Villa with Pool',
            description='Amazing villa with private pool and ocean view',
            location='Miami, FL',
            property_type='villa',
            price_per_night=350.00
        )
        
        # Create bookings
        booking1 = Booking.objects.create(
            property=property1,
            user=guest,
            start_date=datetime.now() + timedelta(days=7),
            end_date=datetime.now() + timedelta(days=14),
            total_price=840.00,
            status='confirmed'
        )
        
        booking2 = Booking.objects.create(
            property=property2,
            user=guest,
            start_date=datetime.now() + timedelta(days=30),
            end_date=datetime.now() + timedelta(days=37),
            total_price=2450.00,
            status='pending'
        )
        
        # Create payments
        Payment.objects.create(
            booking=booking1,
            amount=840.00,
            payment_method='credit_card'
        )
        
        # Create reviews
        Review.objects.create(
            property=property1,
            user=guest,
            rating=5,
            comment='Amazing place! Would definitely stay again.'
        )
        
        # Create messages
        Message.objects.create(
            sender=guest,
            recipient=host,
            message_body='Hi, I have a question about your property'
        )
        
        self.stdout.write(self.style.SUCCESS('Successfully seeded database'))