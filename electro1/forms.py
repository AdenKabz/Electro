from django import forms
from electro1.models import TeamMember, Testimonials, Notifications, UserProfile


class TeamMemberForm(forms.ModelForm):
    class Meta:
        model = TeamMember
        fields = '__all__'

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonials
        fields = '__all__'

class NotificationsForm(forms.ModelForm):
    class Meta:
        model = Notifications
        fields = ['subject', 'message']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'

