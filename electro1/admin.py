from django.contrib import admin
from electro1.models import User, Contact, TeamMember, Testimonials, Notifications, UserProfile

# Register your models here.
admin.site.register(User)
admin.site.register(Contact)
admin.site.register(TeamMember)
admin.site.register(Testimonials)
admin.site.register(Notifications)
admin.site.register(UserProfile)