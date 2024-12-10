from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.mail import send_mail
import json
import requests
from django.http import HttpResponse
from requests.auth import HTTPBasicAuth

from electro1.credentials import MpesaAccessToken, LipanaMpesaPpassword
from electro1.forms import TeamMemberForm, TestimonialForm, NotificationsForm, CustomerForm, UserProfileForm, \
    ProfileSettingsForm, NotificationSettingsForm, SecuritySettingsForm
from electro1.models import Customer, Contact, TeamMember, Testimonials, Notifications, UserProfile, Payment


# Create your views here.
def index(request):
    welcome_message='Welcome to Electro'
    return render(request, 'index.html', {'welcome_message': welcome_message})

def starter(request):
    return render(request, 'starter.html')

def services(request):
    return render(request, 'service-details.html')

def about (request):
    return render(request, 'about.html')

def testimonials(request):
    test = Testimonials.objects.all()
    return render(request, 'testimonials.html', {'test': test})

def team(request):
    team_members=TeamMember.objects.all()
    return render(request, 'team.html', {'team_members': team_members})

def faq(request):
    return render(request, 'faq.html')



def login(request):
    return render(request,'login.html')





@login_required(login_url='login')
def dashboard(request):
    customer = Customer.objects.all()
    user_profile = UserProfile.objects.all()
    return render(request, 'dashboard.html', {'customer': customer, 'user_profile': user_profile})



@login_required(login_url='login')
def edit_profile(request):
   if request.method =="POST":
       customer_form = CustomerForm(request.POST, request.FILES)
       user_profile_form = UserProfileForm(request.POST, request.FILES)
       if user_profile_form.is_valid() and customer_form.is_valid():
           customer_form.save()
           user_profile_form.save()
           return redirect('/dashboard')
   else:
       customer_form = CustomerForm()
       user_profile_form = UserProfileForm()
   return render(request, 'edit_profile.html', {'user_profile_form': user_profile_form, 'customer_form': customer_form})




def some_error_page(request):
    return render(request, 'some_error_page.html')


def signup(request):
    if request.method == 'POST':
        members = Customer(
            name=request.POST['name'],
            email=request.POST['email'],
            username=request.POST['username'],
            password=request.POST['password'],
        )
        members.save()
        return redirect('/login')
    else:
        return render(request, 'signup.html')



def contact (request):
    if request.method == "POST":
        reachout=Contact(
            name=request.POST['name'],
            email=request.POST['email'],
            subject=request.POST['subject'],
            message=request.POST['message']
        )
        reachout.save()
        messages.success(request, 'Thank you for contacting us! We will get back to you as soon as possible.')
        return redirect('/contact')
    else:
        return render(request, 'contact.html')

@login_required (login_url='login')
def customerbase(request):
    if request.method == 'POST':
        if Customer.objects.filter(
                username=request.POST['username'],
                password=request.POST['password']).exists():
            members = Customer.objects.get(
                username=request.POST['username'],
                password=request.POST['password'])
            return render(request, 'customerbase.html', {'members': members})
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

@login_required (login_url='login')
def recent_usage(request):
    return render(request, 'recent_usage.html')

@login_required (login_url='login')
def payment_history(request):
    payments=Payment.objects.all()
    return render(request, 'payment_history.html', {'payments': payments})



@login_required (login_url='login')
def notifications(request):
    notify=Notifications.objects.all()
    return render(request, 'notifications.html', {'notify': notify})

@login_required (login_url='login')
def settings(request):
    return render(request, 'settings.html')

    # profile_form = ProfileSettingsForm()
    # notification_form = NotificationSettingsForm()
    # security_form = SecuritySettingsForm()
    #
    # if request.method == 'POST':
    #     if 'profile_form' in request.POST:
    #         profile_form = ProfileSettingsForm(request.POST, request.FILES)
    #         if profile_form.is_valid():
    #             profile_form.save()
    #             return redirect('settings')
    #     elif 'notification_form' in request.POST:
    #         notification_form = NotificationSettingsForm(request.POST, request.FILES)
    #         if notification_form.is_valid():
    #             notification_form.save()
    #             return redirect('settings')
    #     elif 'security_form' in request.POST:
    #         security_form = SecuritySettingsForm(request.POST, request.FILES)
    #         if security_form.is_valid():
    #             security_form.save()
    #             return redirect('settings')
    #
    # return render(request, 'settings.html', {
    #     'profile_form': profile_form,
    #     'notification_form': notification_form,
    #     'security_form': security_form,
    # })


@login_required (login_url='login')
# Profile Settings View
def profile_settings(request):
    if request.method == 'POST':
        profile_form = ProfileSettingsForm(request.POST, request.FILES)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('/settings')  # Redirect to the settings page after saving
    else:
        profile_form = ProfileSettingsForm()

    return render(request, 'customerbase.html', {'profile_form': profile_form})


# Notification Settings View
def notification_settings(request):
    if request.method == 'POST':
        notification_form = NotificationSettingsForm(request.POST, request.FILES)
        if notification_form.is_valid():
            notification_form.save()
            return redirect('/settings')  # Redirect to the settings page after saving
    else:
        notification_form = NotificationSettingsForm()

    return render(request, 'customerbase.html', {'notification_form': notification_form})


# Security Settings View
def security_settings(request):
    if request.method == 'POST':
        security_form = SecuritySettingsForm(request.POST, request.FILES)
        if security_form.is_valid():
            security_form.save()
            return redirect('/settings')  # Redirect to the settings page after saving
    else:
        security_form = SecuritySettingsForm()

    return render(request, 'customerbase.html', {'security_form': security_form})

@login_required (login_url='login')
def delete_account(request):
    if request.method == 'POST':
        # Logic to delete the account (add actual logic here)
        request.user.delete()
        return HttpResponse("Account deleted successfully!")
    return redirect('/settings')

#Mpesa api views
def token(request):
    consumer_key = 'SwwtjOGZp0PcpqJ5ygkANkVEhLkRm9z3hjE4VAu85WPPsvrl'
    consumer_secret = '1G7LKYNfWxr4xwlGLChfrOagQxQAsVTIAdQzJpvoiUdKSQP037HF3TCyjFA2RADq'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL, auth=HTTPBasicAuth(
        consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token["access_token"]

    return render(request, 'token.html', {"token":validated_mpesa_access_token})

def pay(request):
   if request.method=='POST':
       allpayments=Payment(
           meter_number=request.POST['meter_number'],
           amount=request.POST['amount'],
           phone_number=request.POST['phone']
       )
       allpayments.save()
       return redirect('/payment_history')
   else:
       return render(request, 'pay.html')



def stk(request):
    if request.method =="POST":
        meter_number = request.POST['meter_number']
        phone = request.POST['phone']
        amount = request.POST['amount']
        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {
            "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
            "Password": LipanaMpesaPpassword.decode_password,
            "Timestamp": LipanaMpesaPpassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": LipanaMpesaPpassword.Business_short_code,
            "PhoneNumber": phone,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "Electro",
            "TransactionDesc": "Electricity bill"
        }
        response = requests.post(api_url, json=request, headers=headers)
        return HttpResponse("Payment made successfully. Electricity coming your way shortly.")


#Admin Turf
#Admin Login
# def admin_login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             login(request, user)
#             # Redirect to admin dashboard after successful login
#             return redirect('/admin/adminbase.html')  # Adjust the URL based on your admin panel access
#         else:
#             # Handle invalid login attempt
#             message = 'Invalid username or password.'
#             return render(request, 'admin/admin_login.html', {'message': message})
#     else:
#         return render(request, 'admin/admin_login.html')

@login_required
def adminbase(request):
    return render(request, 'admin/adminbase.html')

def admin_dashboard(request):
    customer_count=Customer.objects.all().count()
    contact_count=Contact.objects.all().count()
    team_count=TeamMember.objects.all().count()
    testimonial_count=Testimonials.objects.all().count()
    notification_count=Notifications.objects.all().count()
    return render(request, 'admin/admin_dashboard.html', {'customer_count': customer_count, 'contact_count': contact_count, 'team_count': team_count, 'testimonial_count': testimonial_count, 'notification_count': notification_count})


# @login_required
# def admin_logout(request):
#     return render(request, 'admin/admin_login.html')

@login_required
def manage_users(request):
    allusers=Customer.objects.all()
    return render(request, 'admin/manage_users.html', {'allusers': allusers})

def delete_user(request, id):
    someone=Customer.objects.get(id=id)
    someone.delete()
    return redirect('/manage_users')

def add_member(request):
    if request.method == 'POST':
        form1 = TeamMemberForm(request.POST, request.FILES)
        if form1.is_valid():
            form1.save()
            return redirect('/team')
    else:
            form1 = TeamMemberForm()
    return render(request, 'admin/manage_team_members.html', {'form1': form1})

def add_testimonial(request):
    if request.method == 'POST':
        form2 = TestimonialForm(request.POST, request.FILES)
        if form2.is_valid():
            form2.save()
            return redirect('/testimonials')
    else:
        form2 = TestimonialForm()
    return render(request, 'admin/manage_testimonials.html', {'form2': form2})

def send_notifications(request):
    if request.method == 'POST':
        form3 = NotificationsForm(request.POST, request.FILES)
        if form3.is_valid():
            form3.save()
            return redirect('/notifications')
    else:
        form3 = NotificationsForm()
    return render(request, 'admin/send_notifications.html', {'form3': form3})

def manage_contacts(request):
    allcontacts=Contact.objects.all()
    return render(request, 'admin/manage_contacts.html', {'allcontacts': allcontacts})


def respond(request, contact_id):
    if request.method == 'POST':
        # Access the contact object based on ID
        retrieved_contact = Contact.objects.get(pk=contact_id)

        # Get the response message from the form (assuming a form)
        response_message = request.POST.get('response_message')

        # Send email to the customer
        send_mail(
            subject='Re: ' + retrieved_contact.subject,  # Subject with prefix
            message=response_message,
            from_email='electro@gmail.com',  # Replace with your email
            recipient_list=[retrieved_contact.email],  # Customer's email
        )

        # Success message (optional)
        messages.success(request, 'Response sent successfully!')

        return redirect('/manage_contacts')  # Redirect after sending
    else:
        # Handle GET requests (optional, e.g., pre-fill a form)
        return redirect('/manage_contacts')  # Or render a form template

