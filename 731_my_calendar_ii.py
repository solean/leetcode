
class MyCalendarTwo:

    def __init__(self):
        self.bookings = []
        self.double_bookings = []

    def book(self, start: int, end: int) -> bool:
        for double_booking in self.double_bookings:
            if start < double_booking[1] and end > double_booking[0]:
                # would be triple booking
                return False

        overlaps = []
        for booking in self.bookings:
            if start < booking[1] and end > booking[0]:
                overlaps.append((max(start, booking[0]), min(end, booking[1])))

        if overlaps:
            for overlap in overlaps:
                self.double_bookings.append((max(start, overlap[0]), min(end, overlap[1])))

        self.bookings.append((start, end))
        return True

