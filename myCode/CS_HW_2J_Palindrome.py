def isPalindrome(word: str) -> bool:
    word: str = ''.join(e for e in word if e.isalnum()).lower()
    return word == word[::-1]

def main() -> None:
    print("Palindrome Tester")
    userInput: str = input("Type a word: ").lower()
    if isPalindrome(userInput):
        print("The word provided is a palindrome.")
    else:
        print("The word provided is not a palindrome.")

if __name__ == '__main__':
    main()