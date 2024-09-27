
class MyCalendar:

    def __init__(self):
        self.bookings = []

    def book(self, start: int, end: int) -> bool:
        for booking in self.bookings:
            if start < booking[1] and end > booking[0]:
                return False

        self.bookings.append((start, end))
        return True

