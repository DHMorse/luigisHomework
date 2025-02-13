# ABC_Corp.py

# This code needs to be cleaned up, it works, but I don't like the structure of it
# I don't think a class is needed for this

class Customer:
    firstName: str = ''
    lastName: str = ''
    address: str = ''
    city: str = ''
    state: str = ''
    zipCode: str = ''
    phoneNumber: str = ''

def main(ABC_names: str = "myCode/ABC_names.txt", ABC_addresses: str = "myCode/ABC_addresses.txt", 
            ABC_phone: str = "myCode/ABC_phone.txt", 
            ABC_customerData: str = "myCode/ABC_Customer_Data.txt"
        ) -> None:
    
    customers: list[str] = []
    
    customerObj = Customer()

    with open(ABC_names, "r") as ABC_names:
        name = ABC_names.readline().strip()
    
    with open(ABC_addresses, "r") as ABC_addresses:
        customerObj.address = ABC_addresses.readline().strip()
        customerObj.city = ABC_addresses.readline().strip()
        line3 = ABC_addresses.readline().strip()
    
    with open(ABC_phone, "r") as ABC_phone:
        customerObj.phoneNumber = ABC_phone.readline().strip()

    for i in range(1000):
        names = name.split()
        
        customerObj.firstName = names[0]
        customerObj.lastName = names[1]
        
        stzip = line3.split()
        
        customerObj.state = stzip[0]
        customerObj.zipCode = stzip[1]
        
        customers.append(customerObj)

    with open(ABC_customerData, "w") as ABC_customerData:
        for customerObj in customers:
            ABC_customerData.write(f"{customerObj.lastName}, {customerObj.firstName}\n")
            ABC_customerData.write(f"{customerObj.address}\n")
            ABC_customerData.write(f"{customerObj.city}, {customerObj.state} {customerObj.zipCode}\n")
            ABC_customerData.write(f"{customerObj.phoneNumber}\n\n")


if __name__ == "__main__":
    main()