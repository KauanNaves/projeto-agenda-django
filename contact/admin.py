from django.contrib import admin
from contact.models import Contact, Category

# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'created_date')
    ordering = ('-id',)
    search_fields = ('first_name', 'last_name', 'email')
    list_per_page = 25
    list_max_show_all = 200
    list_display_links = ('first_name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    ordering = ('-id',)
