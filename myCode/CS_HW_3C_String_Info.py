from typing import Tuple

def getUserString() -> str:
    while True:
        try:
            string: str = input("Enter a word or phrase: ")
            if string == "":
                raise ValueError("String cannot be empty.")
            break
        except Exception as e:
            print(e)
    return string

def getStringInfo(string: str) -> Tuple[int, int, int, int]:
    total_digits: int = 0
    total_letters: int = 0
    for char in string:
        if char.isdigit():
            total_digits += 1

        elif char.isalpha():
            total_letters += 1

    return (len(string), len(string.split(' ')), total_digits, total_letters)

def main() -> None:
    userString: str = getUserString()
    stringInfo: Tuple[int, int, int, int] = getStringInfo(userString)
    print(f"characters: {stringInfo[0]}")
    print(f"words: {stringInfo[1]}")
    print(f"digits: {stringInfo[2]}")
    print(f"letters: {stringInfo[3]}")

if __name__ == '__main__':
    main()