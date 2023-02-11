class TicketConstants:
    OPEN, ACKNOWLEDGED, SOLVED, CLOSED = ('Open', 'Acknowledged', 'Solved', "Closed")

    LOW, MEDIUM, HIGH = ('Low', 'Medium', 'High')

    @classmethod
    def get_status_choices(cls):
        Ticket_Status_Choices = [
            (cls.OPEN, 'open'),
            (cls.ACKNOWLEDGED, 'Acknowledged'),
            (cls.SOLVED, 'Solved'),
            (cls.CLOSED, 'Closed'),
        ]
        return Ticket_Status_Choices

    @classmethod
    def get_priority_choices(cls):
        Priority_Choices = [
            (cls.LOW, 'Low'),
            (cls.MEDIUM, 'Medium'),
            (cls.HIGH, 'High'),

        ]
        return Priority_Choices
