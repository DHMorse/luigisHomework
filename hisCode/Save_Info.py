# Save_Info.py

last_name = input("Last Name: ")
first_name = input("First Name: ")
street_address = input("Street Address: ")
city = input("City: ")
state = input("State: ")
zip_code = input("Zip Code: ")

f = open("addresses.txt", "a")
f.write(f"{last_name}, {first_name}\n{street_address}\n{city}, {state} {zip_code}\n\n")
f.close()
