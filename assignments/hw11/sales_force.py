"""
Name: Ryan Campbell
hw11.py
sales_force.py
Problem: creating classes that are used together
Certification of Authenticity: I, Ryan Campbell, certify this assignment
is entirely my own work.
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>


"""
from sales_person import *


class SalesForce:

    def __init__(self):
        sales_people = []
        self.sales_people = sales_people

    def add_data(self, file_name):
        file_ = open(file_name, "r")
        for line in file_.readlines():
            line = line.split(",")
            sales_person = SalesPerson(int(line[0]), line[1].lstrip())
            split_sales = line[2].lstrip().rstrip().split(" ")
            for i in range(len(split_sales)):
                SalesPerson.enter_sale(sales_person, eval(split_sales[i]))
            self.sales_people.append(sales_person)
# create salesperson from data in line

    def quota_report(self, quota):
        sales_peoples_list = []
        for i in range(len(self.sales_people)):
            employee = self.sales_people[i]
            sales_person_list = []
            sales_person_id = SalesPerson.get_id(employee)
            sales_person_list.append(int(sales_person_id))
            sales_person_name = SalesPerson.get_name(employee)
            sales_person_list.append(sales_person_name)
            total_sales = float(SalesPerson.total_sales(employee))
            sales_person_list.append(total_sales)
            if SalesPerson.met_quota(employee, quota):
                sales_person_list.append(True)
            else:
                sales_person_list.append(False)
            sales_peoples_list.append(sales_person_list)
        return sales_peoples_list

    def top_seller(self):
        top_seller = [""]
        top_total = 0

        for employee in self.sales_people:
            total = SalesPerson.total_sales(employee)
            if total > top_total:
                top_seller.remove(top_seller[0])
                top_seller.append(employee)
                top_total = SalesPerson.total_sales(employee)
            elif total == top_total:
                top_seller.append(employee)
        return top_seller

    def individual_sales(self, employee_id):
        for i in range(len(self.sales_people)):
            employee = self.sales_people[i]
            if employee_id == SalesPerson.get_id(employee):
                return SalesPerson.__str__(employee)
        return None

    def get_sale_frequencies(self):
        dictionary = {}

        keys = []
        for employee in self.sales_people:
            sales = SalesPerson.get_sales(employee)
            for i in range(len(sales)):
                keys.append(sales[i])
        for sale in keys:
            frequency = keys.count(sale)
            dictionary[sale] = frequency
        return dictionary
