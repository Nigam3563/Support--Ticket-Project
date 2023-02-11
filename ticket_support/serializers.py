from rest_framework import serializers, status
from rest_framework.response import Response

from ticket_support.models import SupportTicket


class SupportTicketSerializer(serializers.ModelSerializer):
    # user = serializers.SerializerMethodField()
    #
    # def get_user(self, obj: SupportTicket):
    #     return obj.added_by.__str__()

    class Meta:
        model = SupportTicket
        fields = (
            'id', 'title', 'reference_number', 'module', 'status', 'priority', 'created', 'description',)

        # exclude = ['id']   # we can use both in same places ??
    #
    # def validate(self, attrs):
    #     refrence_number = attrs.get('refrence_number')
    #     if SupportTicket.objects.filter(id=refrence_number).exists():
    #         raise serializers.ValidationError("Please enter another refrence_number")
    #     return attrs

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
