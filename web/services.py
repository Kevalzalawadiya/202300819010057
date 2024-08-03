from django.template import Context
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMessage
from django.conf import settings

class EmailServices:
    
    @classmethod
    def send_inquiry_mail(cls, obj):
        subject = "Thanks for association"
        ctx = {
            'user': obj.first_name + " " + obj.last_name 
        }
        message = get_template('inquire_email.html').render(ctx)
        msg = EmailMessage(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [obj.email],
        )
        msg.content_subtype = "html"  # Main content is now text/html
        msg.send()
        print("Mail successfully sent")
