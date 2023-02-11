from django.contrib import admin
from .models import SupportTicket, TicketLog


# Register your models here.
@admin.register(SupportTicket)
class SupportTicketAdmin(admin.ModelAdmin):
    list_display = ['title', 'reference_number', 'created', 'module']


admin.site.register(TicketLog)
