from rest_framework import routers
from django.urls import path, include

from ticket_support.views import SupportTicketViewset

router = routers.DefaultRouter()
router.register('support_ticket', SupportTicketViewset,basename='support_ticket')

urlpatterns = [
    path('api/', include(router.urls)),
]

