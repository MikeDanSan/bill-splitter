class Bill:
    """
    Object that contains the bill information, such as the total amount and period of the bill.
    """

    def __init__(self, amount: float, period: str):
        self.amount = amount
        self.period = period


class Person:
    """
    Person object that contains the information of the person, such as the name and days in the house and pays a share of the bill.
    """

    def __init__(self, name: str, days_in_house: int):
        self.name = name
        self.days_in_house = days_in_house

    def pay_bill(self, bill):
        return bill.amount / 2


class PdfReport:
    """
    PDF report that generates a report of the people in the house and the amount they owe during a specific period.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate_report(self, person1, person2, bill):
        pass


bill = Bill(120, "March 2021")
michael = Person("Michael", 20)
jamie = Person("Jamie", 25)

print(michael.pay_bill(bill))
