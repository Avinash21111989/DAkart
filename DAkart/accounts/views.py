from email.message import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.conf import settings
from .forms import RegistrationForm
from .models import Account
from django.contrib import messages , auth
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = email.split("@")[0]
            user = Account.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
            user.phone_number = phone_number
            user.save()
            #logic for sending email to verify email address
            current_site  = get_current_site(request)
            print(current_site)
            mail_subject = "DAKart - Please activate your account"
            email_from = settings.EMAIL_HOST_USER
            message = render_to_string('accounts/account_verification_email.html',{
                 'user':user,                         
                 'domain':current_site,
                 'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                 'token':default_token_generator.make_token(user)
            })
            to_email = [email,]
            send_mail(mail_subject,message,email_from,to_email)
            return redirect('/accounts/login?command=verification&email='+email)
    
    form = RegistrationForm()
    context = {
                'form': form,
             }
    return render(request, 'accounts/register.html', context)
             
            
    

def login(request):
    if request.method == 'POST':
        entered_email = request.POST["email"]
        entered_password = request.POST["password"]
        
        user =  auth.authenticate(email=entered_email, password = entered_password)

        if user is not None:
                auth.login(request,user)
                return redirect('welcome')
        else:
                messages.error(request,"Invalid Login Credentials")
                return redirect('login')
    
    return render(request, 'accounts/login.html')

def logout(request):
     auth.logout(request)
     messages.success(request,'You have logged out')
     return redirect('login')
     
def activate(request,uidb64,token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except(TypeError, ValueError , OverflowError, Account.DoesNotExist):
         user = None
    
    if user is not None and default_token_generator.check_token(user,token):
         user.is_active = True
         user.save()
         messages.success(request,"Your account is activated!")
         return redirect('login')
    else:
         messages.error(request,"Invalid activation link")
         return redirect('register')


def dashboard(request):
     return render(request,'accounts/dashboard.html')



