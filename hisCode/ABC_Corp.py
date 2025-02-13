# ABC_Corp.py

class Customer:
    first_name = ""
    last_name = ""
    address = ""
    city = ""
    state = ""
    zip_code = ""
    phone_number = ""

customers = []

f1 = open("ABC_names.txt", "r")
f2 = open("ABC_addresses.txt", "r")
f3 = open("ABC_phone.txt", "r")

# Read the data into a list of Customer objects
i = 0
while i < 1000:
    # get the first and last name
    cust = Customer()
    name = f1.readline().strip()
    names = name.split()
    cust.first_name = names[0]
    cust.last_name = names[1]
    # print(f"{cust.last_name}, {cust.first_name}")
    
    # get the address info
    cust.address = f2.readline().strip()
    cust.city = f2.readline().strip()
    line3 = f2.readline().strip()
    stzip = line3.split()
    cust.state = stzip[0]
    cust.zip_code = stzip[1]
    # print(f"{cust.address}, {cust.city}, {cust.state}, {cust.zip_code}")
    
    # get the phone number
    cust.phone_number = f3.readline().strip()

    customers.append(cust)
    # print(f"{cust.phone_number}")
    i += 1

f1.close()
f2.close()
f3.close()

f4 = open("ABC_Customer_Data.txt", "w")
for cust in customers:
    f4.write(f"{cust.last_name}, {cust.first_name}\n")
    f4.write(f"{cust.address}\n")
    f4.write(f"{cust.city}, {cust.state} {cust.zip_code}\n")
    f4.write(f"{cust.phone_number}\n\n")

f4.close()