from django.contrib import admin

# Register your models here.

from .models import DonationReques


class StudentAdmin(admin.ModelAdmin):
   list_display = ('Firstname', 'Lastname','Address','District','Pincode', 'State','Gender','Bloodgroup','Relative_name','Relationship','Contact','Donate')
   list_filter=('Gender','Donate','Bloodgroup')
   save_as = True
   save_on_top = True
   change_list_template = 'change_list_graph.html'


admin.site.register(DonationReques, StudentAdmin)
