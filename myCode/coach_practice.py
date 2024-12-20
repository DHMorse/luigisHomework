def getUserTemp() -> int:
    while True:
        try:
            userInputTemp: int = int(input("Enter the temperature: "))
            break
        except Exception as e:
            print(e)
    return userInputTemp

def getUserIsRaining() -> bool:
    while True:
        try:
            userInputRaining: str = input("Is it raining? (y/n): ").lower()
            if userInputRaining == 'y' or userInputRaining == 'n':
                break
            else:
                raise ValueError("Please enter 'y' or 'n'.")
        except Exception as e:
            print(e)

    return True if userInputRaining == 'y' else False

def main() -> None:
    userTemp: int = getUserTemp()
    userIsRaning: bool = getUserIsRaining()

    if userTemp > 104 or (userTemp < 32 and userIsRaning is True):
        print("Practice is cancelled.")
    else:
        print("We will have practice.")

if __name__ == '__main__':
    main()