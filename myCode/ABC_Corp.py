# ABC_Corp.py

from typing import List, Dict

class Customer:
    firstName: str = ''
    lastName: str = ''
    address: str = ''
    city: str = ''
    state: str = ''
    zipCode: str = ''
    phoneNumber: str = ''

def extractNames(filename: str) -> List[str]:
    with open(filename, 'r') as namesFile:
        names = namesFile.readlines()
        return [' '.join(name.strip().split()[::-1]) for name in names]

def extractAddresses(filename: str) -> List[Dict[str, str]]:
    addresses = []
    
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    # Ensure the number of lines is a multiple of 3
    if len(lines) % 3 != 0:
        raise ValueError("File format is incorrect. Each address should be three lines.")
    
    for i in range(0, len(lines), 3):
        address = lines[i].strip()
        city = lines[i+1].strip()
        state_zip = lines[i+2].strip().split()
        
        if len(state_zip) != 2:
            raise ValueError(f"Invalid state/ZIP format on line {i+3}: {lines[i+2]}")
        
        state, zip_code = state_zip
        
        addresses.append({
            'address': address,
            'city': city,
            'state': state,
            'zip_code': zip_code
        })
    
    return addresses

def extractPhoneNumbers(filename: str) -> List[str]:
    with open(filename, 'r') as phoneFile:
        phoneNumbers = phoneFile.readlines()
        return [phone.strip() for phone in phoneNumbers]

def writeCustomerData(filepath: str, customers: List[Customer]) -> None:
    with open(filepath, 'w') as customerDataFile:
        for customer in customers:
            customerDataFile.write(f"{customer.lastName}, {customer.firstName}\n")
            customerDataFile.write(f"{customer.address}\n")
            customerDataFile.write(f"{customer.city}, {customer.state} {customer.zipCode}\n")
            customerDataFile.write(f"{customer.phoneNumber}\n\n")

def makeCustomerObjectList(firstAndLastNames: List[str], addresses: List[str], cities: List[str], states: List[str], zipCodes: List[str], 
                            phoneNumbers: List[str]) -> List[Customer]:
    customers: List[str] = []
    
    if not len(firstAndLastNames) == len(addresses) == len(cities) == len(states) == len(zipCodes) == len(phoneNumbers):
        raise ValueError("Data files do not contain the same number of records.")
    
    if not type(firstAndLastNames) == type(addresses) == type(cities) == type(states) == type(zipCodes) == type(phoneNumbers) == list:
        raise ValueError("Data files must be lists of strings.")

    for i in range(len(firstAndLastNames)):
        customerObj = Customer()
        customerObj.firstName = firstAndLastNames[i].split()[0]
        customerObj.lastName = firstAndLastNames[i].split()[1]
        customerObj.address = addresses[i]
        customerObj.city = cities[i]
        customerObj.state = states[i]
        customerObj.zipCode = zipCodes[i]
        customerObj.phoneNumber = phoneNumbers[i]
        customers.append(customerObj)

    return customers

def main(ABC_namesPath: str = "myCode/ABC_names.txt", ABC_addressesPath: str = "myCode/ABC_addresses.txt", 
            ABC_phonePath: str = "myCode/ABC_phone.txt", 
            ABC_customerDataPath: str = "myCode/ABC_Customer_Data.txt"
        ) -> None:
    firstAndLastNames: List[str] = extractNames(ABC_namesPath)

    addressData: List[Dict[str, str]] = extractAddresses(ABC_addressesPath)
    
    addresses = [address['address'] for address in addressData]
    cities = [address['city'] for address in addressData]
    states = [address['state'] for address in addressData]
    zipCodes = [address['zip_code'] for address in addressData]

    phoneNumbers: List[str] = extractPhoneNumbers(ABC_phonePath)

    customers: List[Customer] = makeCustomerObjectList(firstAndLastNames, addresses, cities, states, zipCodes, phoneNumbers)

    writeCustomerData(ABC_customerDataPath, customers)

if __name__ == "__main__":
    main()