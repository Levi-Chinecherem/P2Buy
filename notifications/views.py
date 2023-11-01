from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.views.generic import ListView
from .models import Notification
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.conf import settings 
from django.dispatch import receiver

@login_required
def mark_notification_as_read(request, notification_id):
    notification = get_object_or_404(Notification, id=notification_id)

    if notification.recipient == request.user:
        notification.read = True
        notification.save()

        # Send an email notification
        subject = 'Notification Read'
        message = f'Your notification with ID {notification.id} has been marked as read.'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [notification.recipient.email]
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)

    return redirect('notification_list')

@login_required
def create_notification(user, message):
    notification = Notification(user=user, message=message, timestamp=timezone.now())
    notification.save()

# Example custom message functions for different actions
def order_status_message(order_id, new_status):
    return f'Your order with ID {order_id} has a new status: {new_status}.'

def group_change_message(group_name, action):
    return f'The group "{group_name}" has been {action}.'

@login_required
def notification_list(request):
    notifications = Notification.objects.filter(recipient=request.user).order_by('-timestamp')
    return render(request, 'notifications/notification_list.html', {'notifications': notifications})

class NotificationListView(ListView):
    model = Notification
    template_name = 'notifications/notification_list.html'
    context_object_name = 'notifications'
    ordering = ['-timestamp']
    paginate_by = 10

@receiver(post_save, sender=Notification)
def create_notification_and_send_email(sender, instance, created, **kwargs):
    if created:
        notification = instance
        recipient = notification.user

        subject = 'Notification from Your Website'
        message = notification.message  # Use the custom message
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [recipient.email]

        send_mail(subject, message, from_email, recipient_list, fail_silently=False)

# Connect the signal to the function
post_save.connect(create_notification_and_send_email, sender=Notification)
