from django.contrib import admin
from .models import UserData, Ticketing

# Register your models here.
class TicketingAdminInline(admin.TabularInline):
    model = Ticketing
    readonly_fields = ('lineitem_total',)


class UserDataAdmin(admin.ModelAdmin):
    inlines = (TicketingAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total',)

    fields = ('order_number', 'user_profile', 'date', 'full_name',
              'email', 'phone_number', 'user_id',
              'date_of_birth', 'delivery_cost',
              'order_total', 'grand_total',)

    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'delivery_cost',
                    'grand_total',)

    ordering = ('-date',)

admin.site.register(UserData, UserDataAdmin)