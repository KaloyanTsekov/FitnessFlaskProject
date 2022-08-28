from enum import Enum


class UserRole(Enum):
    regular = "Regular"
    moderator = "Moderator"
    admin = "Admin"


class BodySection(Enum):
    legs = "Legs"
    arms = "Arms"
    shoulders = "Shoulders"
    chest = "Chest"
    back = "Back"
    abs = "ABS"


class DaysFromTheWeekend(Enum):
    monday = 'Monday'
    tuesday = 'Tuesday'
    wednesday = 'Wednesday'
    thursday = 'Thursday'
    friday = 'Friday'
    saturday = 'Saturday'
    sunday = 'Sunday'
