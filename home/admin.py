from django.contrib import admin
from .models import ContactForm


class ContactFormAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'phone',
        'title',
        'description',
        'contact_method',
        'created_at'
    )


admin.site.register(ContactForm, ContactFormAdmin)
