from django.contrib.auth.models import User
from django.db import models
from django_lifecycle import LifecycleModelMixin, AFTER_CREATE, hook

from lib.constant import TicketConstants


# Create your models here.

class SupportTicket(LifecycleModelMixin, models.Model):
    reference_number = models.CharField(max_length=200, verbose_name='Reference Number')
    title = models.CharField(max_length=255, verbose_name='Title')
    module = models.CharField(max_length=255, verbose_name='Module')
    status = models.CharField(max_length=20, choices=TicketConstants.get_status_choices(),
                              default=TicketConstants.OPEN)
    priority = models.CharField(max_length=20, choices=TicketConstants.get_priority_choices(),
                                default=TicketConstants.LOW)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    description = models.CharField(max_length=255, verbose_name='Description')
    # added_by = models.ForeignKey(User, related_name="ticket_added_by", on_delete=models.SET_NULL, blank=True,
    #                              null=True)

    def __str__(self):
        return f'{self.reference_number}-{self.module}'

    @hook(AFTER_CREATE)
    def after_create_log(self):
        self.add_ticket_log(TicketConstants.OPEN, self.priority)

    def add_ticket_log(self, message, status, user=None):
        ticket_log = TicketLog.objects.create(ticket=self, message=message, ticket_status=status)
        return ticket_log


class TicketLog(models.Model):
    ticket = models.ForeignKey(SupportTicket, related_name="ticket_logs", verbose_name="Ticket",
                               on_delete=models.CASCADE)
    ticket_status = models.CharField(
        choices=TicketConstants.get_status_choices(), default=TicketConstants.OPEN,
        verbose_name="Ticket Status", max_length=50)
    message = models.TextField(verbose_name="Message")
    # added_by = models.ForeignKey(
    #     User, related_name="ticket_log_by", verbose_name="Added By",
    #     on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.message}'
