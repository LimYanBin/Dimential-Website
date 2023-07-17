from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from celery import shared_task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

@shared_task
def send_email_task():
    
    logger.info("Starting to send emails...")
    for user in User.objects.all():
        email = user.email
        html_template = 'weeklyEmail.html'
        html_message = render_to_string(html_template)
        subject = "Weekly update from Dementia Malaysia"
        email_from = settings.EMAIL_HOST_USER
        receiver = email
        message = EmailMessage(subject, html_message, email_from, [receiver])
        message.content_subtype = 'html'
        message.send()

    logger.info("Finished sending emails.")

