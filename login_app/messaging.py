from django.core.mail import send_mail


def email_message(message_dict):
   contents = f"""
   Hi, a password reset have been requested for your charityfinder.com account.
   Your token is: {message_dict['token']}
   """
   send_mail(
      'Password Reset Token',
      contents,
      'daneskildsen1234@gmail.com',
      [message_dict['email']],
      fail_silently=False
   )
