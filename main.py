from abc import ABC, abstractmethod

# Product
class MentoringSlot(ABC):
    @abstractmethod
    def get_details(self):
        pass


# Concrete Products
class OnlineSlot(MentoringSlot):
    def get_details(self):
        return "Online Mentoring Slot"


class CampusSlot(MentoringSlot):
    def get_details(self):
        return "On-Campus Mentoring Slot"


# Factory
class SlotFactory:
    def create_slot(self, slot_type):
        if slot_type == "online":
            return OnlineSlot()
        elif slot_type == "campus":
            return CampusSlot()


# Main
factory = SlotFactory()

slot1 = factory.create_slot("online")
slot2 = factory.create_slot("campus")

print(slot1.get_details())
print(slot2.get_details())
