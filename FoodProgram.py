import FoodClass as fc 

# this dictionary represents transactions. The key of the dictionary is the transaction identifier.
# The Value of the dictionary is a list. The elements in each list are -
# ['Date', 'Name of item', 'Cost', 'customerid' ]

dict = {
            'trans1':['2/15/2023','The Lone Patty',17,569],
            'trans2':['2/15/2023','The Octobreakfast',18,569],
            'trans3':['2/15/2023','The Octoveg',16,570],
            'trans4':['2/15/2023','The Octoburger',20,570],
}

order_total = 0
order_total2 = 0
discount = .20


customer1 = fc.Customer(570,'Danni Sellyar', '97 Mitchell Way Hewitt Texas 7612', 'dsellyarft@gmpg.org','254-555-9362', False)

customer2 = fc. Customer (569, 'Aubree Himsworth', '1172 Molton Hill Waco Texas 76710','ahimsworthfs@list-manage.com', '254-555-2273', True)

# Customer 1
print(f"Customer Name: {customer1.get_name()}")
print(f"Phone: {customer1.get_phone()}")


for trans in dict:
    customer_trans = fc.Transaction(dict[trans][0], dict[trans][1], dict[trans][2], dict[trans][3])
    if (customer_trans.get_customerid() == customer1.get_customerid()):
        order_total += customer_trans.get_cost()
        print((f"Order Item: {customer_trans.get_iName()}") + '  ' + f"Price: {customer_trans.get_cost():.2f}") 
        if (customer1.get_member_status() == True):
            discount1 = (0.2 * customer_trans.get_cost())
    

print(f"Total Cost: ${order_total:.2f}")

total_cost_after_discount = order_total - discount

if (customer1.get_member_status() == True):
    print(f"Member Discount: ${discount:.2f}")
    print(f"Total Cost after discount: ${total_cost_after_discount:.2f}")
    


print('\n')



# Customer 2 
print(f"Customer Name: {customer2.get_name()}")
print(f"Phone: {customer2.get_phone()}")

for trans in dict:
    customer_trans = fc.Transaction (dict[trans][0], dict[trans][1], dict[trans][2], dict[trans][3])
    if (customer_trans.get_customerid() == customer2.get_customerid()):
        order_total2 += customer_trans.get_cost()
        print((f"Order Item: {customer_trans.get_iName()}") + '  ' + f"Price: {customer_trans.get_cost():.2f}")
        if (customer2.get_member_status() == True):
            discount2 = (0.2 * order_total2)


print(f"Total Cost: ${order_total2:.2f}")

total_cost_after_discount2 = order_total2 - discount2

if (customer2.get_member_status() == True):
    print(f"Member Discount: ${discount2:.2f}")
    print(f"Total Cost after discount: ${total_cost_after_discount2:.2f}")
    
