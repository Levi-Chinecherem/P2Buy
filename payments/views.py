from django.shortcuts import render, redirect, get_object_or_404
import requests
from django.conf import settings
from groups.models import Order  # Import the CheckoutForm from your groups app

def initiate_payment(request, order_id):
    # Define the Payoneer API endpoint for initiating payments
    payoneer_api_url = f'{settings.PAYONEER_API_BASE_URL}payments'

    # Fetch the order object based on the provided order_id
    order = get_object_or_404(Order, id=order_id)

    # Construct the payment request data from the order details
    payment_data = {
        'amount': order.amount,
        'currency': 'NGN',  # Adjust as needed
        'recipient_email': order.recipient_email,
        # Add more payment details as needed
    }

    # Set up the Payoneer API request headers
    headers = {
        'Authorization': f'Bearer {settings.PAYONEER_API_KEY}',
    }

    # Make a POST request to initiate the payment
    response = requests.post(payoneer_api_url, json=payment_data, headers=headers)

    # Check the response for success or failure
    if response.status_code == 200:
        # Payment initiated successfully
        context = {'status': 'Payment initiated successfully'}
        template_name = 'payments/payment_success.html'
    else:
        # Payment initiation failed
        context = {'status': 'Payment initiation failed'}
        template_name = 'payments/payment_failure.html'

    return render(request, template_name, context)
