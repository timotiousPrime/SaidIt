from django.contrib import admin
from .models import Interest, Job_Title, User_Profile, Employment_History
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class EmploymentHistoryInline(admin.StackedInline):
    model = Employment_History
    extra = 1
    can_delete = False
    verbose_name_plural = "employment history"


class UserProfileInline(admin.StackedInline):
    model = User_Profile
    can_delete = False
    verbose_name_plural = "user profile"


class UserAdmin(BaseUserAdmin):
    model = User
    inlines = [UserProfileInline, EmploymentHistoryInline]



# Unregister initial User so we can update the modified User for admin
admin.site.unregister(User)
admin.site.unregister(Group)
# Reregister User and profile
admin.site.register(User, UserAdmin)

# register the UserProfileAdmin that will display the employment history included

admin.site.register(Interest)
admin.site.register(User_Profile )
admin.site.register(Job_Title)
admin.site.register(Employment_History)
