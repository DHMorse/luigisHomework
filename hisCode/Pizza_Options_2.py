def display_pizza_sizes():
    print("PIZZA SIZES")
    print(" 6 inch:  $5.00")
    print("10 inch:  $8.00")
    print("14 inch: $12.00")
    print("18 inch: $15.00")
    print()

def display_toppings():
    print("TOPPINGS")
    print("Pepperoni: $0.75")
    print("Mushrooms: $0.50")
    print("Sausage:   $0.75")
    print("Peppers:   $0.50")
    print()

def display_drink_sizes():
    print("DRINK SIZES")
    print("Small:   $1.29")
    print("Medium:  $1.79")
    print("Large:   $2.19")
    print()

running = True

# main loop
while(running):
    print("Main Menu:")
    print("----------")
    print("1: Display pizza sizes")
    print("2: Display toppings")
    print("3: Display drink sizes")
    print("4: Exit")
    choice = input("> ")
    if choice == "1":
        display_pizza_sizes()
    elif choice == "2":
        display_toppings()
    elif choice == "3":
        display_drink_sizes()
    elif choice == "4":
        running = False

print("Exiting")

