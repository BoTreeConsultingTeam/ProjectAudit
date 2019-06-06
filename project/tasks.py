import string
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

from celery import shared_task

@shared_task
def mails(sender):
    subject = 'Project assigned'
    message = 'Hi '+str(sender['username'])+" \nYou have been assigned a Project named "+str(sender['title'])+" \n Project details are as: "+str(sender['abstract'])
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [sender['email']]
    send_mail( subject, message, email_from, recipient_list )