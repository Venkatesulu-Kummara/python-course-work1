class Redbus:

    bus = {i: "Available" for i in range(1, 11)}

    def dispalyseats(self):
        print("------------------- XYZ BUS ---------------------")

        for i in Redbus.bus:
            print(i, Redbus.bus[i])

    def booking(self, seatno, username):

        if Redbus.bus[seatno] == "Available":
            Redbus.bus[seatno] = username
            print(f"Your seat - {seatno} is successfully booked")

        else:
            print(f"Your seat - {seatno} is already booked")


class user(Redbus):

    def __init__(self, name, email, phoneno):
        self.name = name
        self.email = email
        self.phono = phoneno


class Driver(Redbus):

    def __init__(self, name, phoneno, email, license_no, salary):
        self.name = name
        self.phoneno = phoneno
        self.email = email
        self.license_no = license_no
        self.__salary = salary

    def display_driver(self):

        print("\n--------- DRIVER DETAILS ---------")
        print("Name :", self.name)
        print("Phone:", self.phoneno)

        print("\n--------- BOOKED SEATS ---------")

        for seat in Redbus.bus:

            if Redbus.bus[seat] != "Available":
                print("Seat", seat, ":", Redbus.bus[seat])


shulu = user("shulu", "shulu@gmail.com", 7896778899)

driver = Driver(
    "Ramesh",
    9876543210,
    "ramesh@gmail.com",
    "DL123456",
    30000
)

shulu.dispalyseats()

shulu.booking(7, shulu.name)

shulu.dispalyseats()

shulu.booking(7, shulu.name)

driver.display_driver()
