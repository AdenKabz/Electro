from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
import json
import requests
from django.http import HttpResponse
from requests.auth import HTTPBasicAuth

from electro1.credentials import MpesaAccessToken, LipanaMpesaPpassword
from electro1.forms import TeamMemberForm, TestimonialForm, NotificationsForm, UserProfileForm
from electro1.models import User, Contact, TeamMember, Testimonials, Notifications, UserProfile


# Create your views here.
def index(request):
    welcome_message='Welcome to Electro'
    return render(request, 'index.html', {'welcome_message': welcome_message})

def starter(request):
    return render(request, 'starter.html')

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

@login_required (login_url='login')
def dashboard (request):
    profile = UserProfile.objects.all()
    return render(request, 'dashboard.html', {'profile': profile})

@login_required (login_url='login')
def edit_profile(request):
    if request.method == 'POST':
        form4 = UserProfileForm(request.POST, request.FILES)
        if form4.is_valid():
            form4.save()
            return redirect('/dashboard')
    else:
            form4 = UserProfileForm()
    return render(request, 'admin/manage_team_members.html', {'form4': form4})

def signup (request):
    if request.method == 'POST':
        members=User(
            name=request.POST['name'],
            email=request.POST['email'],
            username=request.POST['username'],
            password=request.POST['password']
        )
        members.save()
        return redirect('/login')
    else:
        return render(request, 'signup.html')

def login (request):
    return render(request, 'login.html')

@login_required (login_url='login')
def payment (request):
    return render(request, 'payment.html')

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
    if request.method == "POST":
        if User.objects.filter(
                username=request.POST['username'],
                password=request.POST['password']
        ).exists():
            return render(request, 'customerbase.html')
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

@login_required (login_url='login')
def recent_usage(request):
    return render(request, 'recent_usage.html')

@login_required (login_url='login')
def payment_history(request):
    return render(request, 'payment_history.html')

@login_required (login_url='login')
def notifications(request):
    notify=Notifications.objects.all()
    return render(request, 'notifications.html', {'notify': notify})

@login_required (login_url='login')
def settings(request):
    return render(request, 'settings.html')

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
   return render(request, 'payment.html')



def stk(request):
    if request.method =="POST":
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
def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to admin dashboard after successful login
            return redirect('/admin/adminbase.html')  # Adjust the URL based on your admin panel access
        else:
            # Handle invalid login attempt
            message = 'Invalid username or password.'
            return render(request, 'admin/admin_login.html', {'message': message})
    else:
        return render(request, 'admin/admin_login.html')

@login_required
def adminbase(request):
    return render(request, 'admin/adminbase.html')

@login_required
def admin_logout(request):
    return render(request, 'admin/admin_login.html')

@login_required
def manage_users(request):
    allusers=User.objects.all()
    return render(request, 'admin/manage_users.html', {'allusers': allusers})

def delete_user(request, id):
    someone=User.objects.get(id=id)
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

def admin_dashboard(request):
    return render(request, 'admin/admin_dashboard.html')

