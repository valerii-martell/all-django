import os
from email.mime.image import MIMEImage

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.views import generic

from . import forms
from .forms import UserSignUpForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.core.mail import EmailMessage, send_mail, EmailMultiAlternatives

from django.conf import settings

from .token_generator import account_activation_token


class Index(generic.TemplateView):
    template_name = 'emails_index.html'


class ShowMailView(generic.TemplateView):
    template_name = 'hello_email_to_response.html'

    def get_context_data(self, **kwargs):
        context = {'my_name': 'All Django'}
        return context


class SendMailView(generic.TemplateView):
    mail_form = forms.SendMailForm

    def _logo_data(self, image_name):
        print(image_name)
        with open(os.path.join(settings.MEDIA_ROOT, 'img', image_name), 'rb') as f:
            logo_data = f.read()
        logo = MIMEImage(logo_data)
        logo.add_header('Content-ID', f'<{image_name}>')
        logo.add_header('Content-Disposition', 'inline', filename=image_name)
        return logo

    def post(self, request):
        form = forms.SendMailForm(request.POST)
        if form.is_valid():
            # plain_message = render_to_string('templates/email.txt', {'some_params': some_params})
            # html_message = render_to_string('hello_email.html', {'my_name': 'All Django'})
            # receiver = form.cleaned_data.get('receiver')
            # send_mail('All Django - test email', 'Some text', settings.EMAIL_HOST, [receiver],
            # html_message=html_message)
            receiver = form.cleaned_data.get('receiver')
            html_content = render_to_string('hello_email.html')

            email_message = EmailMultiAlternatives(subject='Happy New Year',
                                                   body='new year event',
                                                   from_email=settings.EMAIL_HOST,
                                                   to=[receiver])
            email_message.attach_alternative(html_content, "text/html")
            email_message.mixed_subtype = 'related'
            for image in os.listdir(os.path.join(settings.MEDIA_ROOT, 'img')):
                email_message.attach(self._logo_data(image))
            email_message.send(fail_silently=False)
            return HttpResponse("The message has been sent successfully")
        else:
            return HttpResponse("Incorrect email")

    def get(self, request):
        context = {
            'mail_form': self.mail_form
        }
        return render(request, 'send_mail_form.html', context)


def usersignup(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            email_subject = 'Activate Your Account'
            message = render_to_string('activate_account.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(email_subject, message, to=[to_email])
            email.send()
            return HttpResponse(
                'We have sent you an email, please confirm your email address to complete your registration')
    else:
        form = UserSignUpForm()
    return render(request, 'signup.html', {'form': form})


def activate_account(request, uidb64, token):
    try:
        uid = force_bytes(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return HttpResponse('Your account has been activated successfully')
    else:
        return HttpResponse('Activation link is invalid!')
