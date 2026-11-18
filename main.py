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


# Observer Pattern

class Student:
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(self.name, "received alert:", message)


class Mentor:
    def __init__(self):
        self.students = []

    def subscribe(self, student):
        self.students.append(student)

    def unsubscribe(self, student):
        if student in self.students:
            self.students.remove(student)

    def notify(self):
        for student in self.students:
            student.update("New appointment available!")


# Create objects
mentor = Mentor()

s1 = Student("Alice")
s2 = Student("Bob")

# Subscribe Alice
mentor.subscribe(s1)

# Send notification
mentor.notify()
