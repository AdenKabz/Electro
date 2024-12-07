"""
URL configuration for Electro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from electro1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('starter/', views.starter, name='starter'),
    path('about/', views.about, name='about'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('team/', views.team, name='team'),
    path('faq/', views.faq, name='faq'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('contact/', views.contact, name='contact'),
    path('customerbase/', views.customerbase, name='customerbase'),
    path('recent_usage/', views.recent_usage, name='recent_usage'),
    path('payment_history/', views.payment_history, name='payment_history'),
    path('notifications/', views.notifications, name='notifications'),
    path('settings/', views.settings, name='settings'),

#Mpesa api urls
    path('pay/', views.pay, name='pay'),
    path('stk/', views.stk, name='stk'),
    path('token/', views.token, name='token'),

    #admin urls
    path('admin_login/', views.admin_login, name='admin_login'),
    path('adminbase/', views.adminbase, name='adminbase'),
    path('admin_logout/', views.admin_logout, name='admin_logout'),
    path('manage_users/', views.manage_users, name='manage_users'),
    path('delete1/<int:id>', views.delete_user),
    path('teammembers/', views.add_member, name='add_member'),
    path('manage_testimonials/', views.add_testimonial, name='add_testimonial'),
    path('send_notifications/', views.send_notifications, name='send_notifications'),
    path('manage_contacts/', views.manage_contacts, name='manage_contacts'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
]
