import pandas as pd

df = pd.read_csv("hotels.csv", dtype={"id": str})
df_cards = pd.read_csv("cards.csv", dtype=str).to_dict(orient="records")
df_card_security = pd.read_csv("card_security.csv", dtype=str)


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_ID = hotel_id
        self.hotel_name = df.loc[df["id"] == self.hotel_ID, "name"].squeeze()

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


class SpaHotel(Hotel):
    def book_spa_package(self):
        pass


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel_object = hotel_object

    def generate(self):
        content = f"""
        Thank you for your reservation!
        Here are your booking data:
        Name: {self.customer_name}
        Hotel name: {self.hotel_object.hotel_name}
        """

        return content


class CreditCard:
    def __init__(self, number, expiration, holder, cvc):
        self.card_number = number
        self.expiration = expiration
        self.holder_name = holder
        self.cvc = cvc

    def validate(self):
        card_data = {"number": self.card_number, "expiration": self.expiration, "holder": self.holder_name, "cvc": self.cvc}
        if card_data in df_cards:
            return True
        else:
            return False


class SecureCreditCard(CreditCard):
    def authenticate(self, given_password):
        password = df_card_security.loc[df_card_security["number"] == self.card_number, "password"].squeeze()
        if password == given_password:
            return True
        else:
            return False


class SpaTicket:
    def __init__(self, customer_name, spa_hotel_object):
        self.customer_name = customer_name
        self.spa_hotel_object = spa_hotel_object

    def generate(self):
        content = f"""
        Thank you for your reservation!
        Here are your spa booking data:
        Name: {self.customer_name}
        Hotel name: {self.spa_hotel_object.hotel_name}
        """

        return content


if __name__ == '__main__':
    print(df)
    user_hotel_id = input("Enter the ID of the hotel: ")
    hotel = Hotel(user_hotel_id)
    if hotel.available():
        card_number = input("Enter card details: \nCard Number: ")
        card_expiration = input("Card Expiration: ")
        card_holder = input("Card Holder: ")
        card_cvc = input("Card CVC: ")
        credit_card = SecureCreditCard(card_number, card_expiration, card_holder, card_cvc)
        if credit_card.validate():
            user_password = input("Enter authentication password: ")
            if credit_card.authenticate(user_password):
                hotel.book()
                name = input("Enter your name: ")
                reservation_ticket = ReservationTicket(name, hotel)
                r_ticket = reservation_ticket.generate()
                print(r_ticket)
            else:
                print("Credit card authentication failed.")
        else:
            print("There was a problem with your payment")
    else:
        print("Hotel is not free")
    print(df)
