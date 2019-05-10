import string
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

from celery import shared_task

@shared_task
def mails(sender):
    subject = 'Audit Report'
    message = 'Hi '+str(sender['lead_username'])+" and "+str(sender['admin_username'])+" \nYour Audit report "+str(sender['title'])+" generated on "+str(sender['date'])+" has general comments :\n"+str(sender['comment'])+" \n And your general rating is: "+str(sender['rating'])
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [sender['lead_email'],sender['admin_email']]
    send_mail( subject, message, email_from, recipient_list )