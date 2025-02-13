# Happy_Birthday_v2.py

def printHappyBirthdayMessage(name: str) -> None:
    print("Happy birthday to you")
    print("Happy birthday to you")
    print(f"Happy birthday dear {name}")
    print("Happy birthday to you")
    print("")

def main():
    userInputName: str = input("Your name? ")
    printHappyBirthdayMessage(userInputName)

if __name__ == "__main__":
    main()