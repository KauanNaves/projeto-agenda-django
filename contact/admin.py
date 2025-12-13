from django.contrib import admin
from contact.models import Contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'created_date')
    ordering = ('-id',)
    search_fields = ('first_name', 'last_name', 'email')
    list_per_page = 25
    list_max_show_all = 200
    list_display_links = ('first_name',)


admin.site.register(Contact, ContactAdmin)