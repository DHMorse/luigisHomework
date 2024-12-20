def getUserString() -> str:
    while True:
        try:
            string: str = input("Type Something: ")
            break
        except Exception as e:
            print(e)
    return string

def main() -> None:
    userString: str = getUserString()
    print(f"You typed: {userString}")

if __name__ == '__main__':
    main()
    