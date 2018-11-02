from django.contrib import admin

# Register your models here.

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserAdminCreationForm, UserAdminChangeForm
from .models import GuestEmail, Organ, DonateOrgan, DoctorRequestOrgan
from .models import Hospital, Doctor, OdatsSummary, AssingedOrgans


User = get_user_model()

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'admin')
    list_filter = ('admin', 'staff', 'active')
    fieldsets = (
        (None, {'fields': ('full_name', 'email', 'password')}),
       # ('Full name', {'fields': ()}),
        ('Permissions', {'fields': ('admin', 'staff', 'active',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    search_fields = ('email', 'full_name',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)

# Remove Group Model from admin. We're not using it.
admin.site.unregister(Group)

class ReportsAdmin(admin.ModelAdmin):
    change_list_template = 'admin/odats_summary_change_list.html'

    def changelist_view(self, request):
        response = super().changelist_view(
            request)
        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response

        objs = {
            'organs' : Organ.objects.all(),
            'assigned' : AssingedOrgans.objects.all()
        }

        response.context_data['summary'] = objs
        return response


admin.site.register(OdatsSummary, ReportsAdmin)

admin.site.register(Organ)
admin.site.register(DonateOrgan)
admin.site.register(DoctorRequestOrgan)
admin.site.register(AssingedOrgans)
admin.site.register(Hospital)
admin.site.register(Doctor)