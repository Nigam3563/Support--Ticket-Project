from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter, OrderingFilter

# from ticket_support.filters import SupportTicketFilter
from ticket_support.models import SupportTicket
from ticket_support.serializers import SupportTicketSerializer


class SupportTicketViewset(ModelViewSet):
    serializer_class = SupportTicketSerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    search_fields = ('title', 'id', 'reference_number')

    # filterset_class = SupportTicketFilter
    #

    def get_queryset(self):
        print('USER IS --->', self.request.user)
        support_ticket = SupportTicket.objects.all()
        return support_ticket
    # def perform_create(self, serializer):
    #     user = self.request.user
    #     if user:
    #         serializer.save(added_by=user)
    #     else:
    #         return Response(status=400)

    def get_serializer_context(self):
        context = super(SupportTicketViewset, self).get_serializer_context()
        context['user'] = self.request.user
        # print("CONTEXT IS --->", context['view'])
        return context
