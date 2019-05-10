import string
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

from celery import shared_task

@shared_task
def mails(sender):
	subject = 'Team Lead assigned'
	message = ' Congrats you are now registered to Botree and been assigned post of Team Lead '
	email_from = settings.EMAIL_HOST_USER
	recipient_list = [sender]

	send_mail( subject, message, email_from, recipient_list )