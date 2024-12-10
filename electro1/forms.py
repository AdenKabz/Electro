from django import forms
from electro1.models import TeamMember, Testimonials, Notifications, Customer, UserProfile, SecuritySettings, \
    NotificationSettings, ProfileSettings


class TeamMemberForm(forms.ModelForm):
    class Meta:
        model = TeamMember
        fields = '__all__'
        widgets = {
            'image': forms.ClearableFileInput(attrs={'accept': 'image/*'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        }

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonials
        fields = '__all__'
        widgets = {
            'testimonial': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'image': forms.FileInput(attrs={'accept': 'image/*'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'})
        }

class NotificationsForm(forms.ModelForm):
    class Meta:
        model = Notifications
        fields = ['subject', 'message']
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'username', 'password']
        widgets={
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_pic', 'phone_number', 'address', 'meter_number']
        widgets={
            'profile_pic': forms.FileInput(attrs={'accept': 'image/*'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'meter_number': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ProfileSettingsForm(forms.ModelForm):
    class Meta:
        model = ProfileSettings
        fields = ['name', 'email', 'phone_number']
        widgets={
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
        }


class NotificationSettingsForm(forms.ModelForm):
    class Meta:
        model = NotificationSettings
        fields = ['email_notifications', 'sms_notifications']
        widgets={
            'email_notifications': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'sms_notifications': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class SecuritySettingsForm(forms.ModelForm):
    class Meta:
        model = SecuritySettings
        fields = ['two_factor_auth', 'change_password']
        widgets={
            'two_factor_auth': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'change_password': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
