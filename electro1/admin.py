from django.contrib import admin
from electro1.models import Customer, Contact, TeamMember, Testimonials, Notifications, UserProfile, Payment, \
    ProfileSettings, NotificationSettings, SecuritySettings

# Register your models here.
admin.site.register(Customer)
admin.site.register(Contact)
admin.site.register(TeamMember)
admin.site.register(Testimonials)
admin.site.register(Notifications)
admin.site.register(UserProfile)
admin.site.register(Payment)
admin.site.register(ProfileSettings)
admin.site.register(NotificationSettings)
admin.site.register(SecuritySettings)

