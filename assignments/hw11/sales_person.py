"""
Name: Ryan Campbell
hw11.py
sales_person.py
Problem: creating classes that are used together
Certification of Authenticity: I, Ryan Campbell, certify this assignment
is entirely my own work.
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>


"""


class SalesPerson:

    def __init__(self, employee_id, name):
        sales = []
        self.sales = sales
        self.employee_id = employee_id
        self.name = name

    def get_id(self):
        return self.employee_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def enter_sale(self, sale):
        self.sales.append(sale)

    def total_sales(self):
        total = 0
        for i in range(len(self.sales)):
            sale = self.sales[i]
            total += float(sale)
        return total

    def get_sales(self):
        return self.sales

    def met_quota(self, quota):
        if self.total_sales() >= quota:
            return True
        return False

    def compare_to(self, other):
        total_sales_other = SalesPerson.total_sales(other)
        if total_sales_other > self.total_sales():
            return -1
        if self.total_sales() > total_sales_other:
            return 1
        if self.total_sales() == total_sales_other:
            return 0

    def __str__(self):
        return "{}-{}: {}".format(self.employee_id, self.name, self.total_sales())
