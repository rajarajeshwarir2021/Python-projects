import pandas as pd
from abc import ABC, abstractmethod

df = pd.read_csv("hotels.csv", dtype={"id": str})


class Hotel:
    # class variables
    water_mark = "The Real Estate Company"

    def __init__(self, hotel_id):
        # Instance variables
        self.hotel_ID = hotel_id
        self.hotel_name = df.loc[df["id"] == self.hotel_ID, "name"].squeeze()

    # Instance method: methods related to a particular instance
    def available(self):
        """Checks if the Hotel is available"""
        availability = df.loc[df["id"] == self.hotel_ID, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False

    def book(self):
        """Book a Hotel by changing its availability to 'no' """
        df.loc[df["id"] == self.hotel_ID, "available"] = "no"
        df.to_csv("hotels.csv", index=False)

    # Class method: methods somehow related to class but not to a single particular instance
    @classmethod
    def get_hotel_count(cls, data):
        return len(data)

    # Magic methods
    def __eq__(self, other):
        if self.hotel_ID == other.hotel_ID:
            return True
        else:
            return False

    def __add__(self, other):
        total = self.price + other.price
        return total


# Abstract class: its aim is to define a structure, methods defined in abstract class must be implemented in the child class
class Ticket(ABC):

    @abstractmethod
    def generate(self):
        pass

class ReservationTicket(Ticket):
    def __init__(self, customer_name, hotel_object):
        # Instance variables
        self.customer_name = customer_name
        self.hotel_object = hotel_object

    def generate(self):
        content = f"""
        Thank you for your reservation!
        Here are your booking data:
        Name: {self.the_customer_name}
        Hotel name: {self.hotel_object.hotel_name}
        """

        return content

    @property
    def the_customer_name(self):
        name = self.customer_name.strip()
        name = name.title()

        return name

    # Static method: its like a function and has not reference to the class or its instance
    @staticmethod
    def convert(amount):
        return amount * 1.2


class DigitalTicket(Ticket):
    def generate(self):
        print("Hello, this is your digital ticket.")

    def download(self):
        pass