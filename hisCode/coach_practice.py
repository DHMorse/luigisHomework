temp = int(input("Temperature: "))
rain = input("Is it raining? Type Y or N: ")

if temp > 104 or (temp < 32 and rain == "Y"):
    print("Practice is cancelled.")
else:
    print("We will have practice.")
