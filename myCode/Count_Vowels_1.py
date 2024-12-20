import os
from typing import Dict

def getUserFilePath() -> str:
    while True:
        try:
            userInputFilePath: str = input("Enter the path to the file you would like to open press enter for default: ")
            if userInputFilePath == "":
                userInputFilePath = "hisCode/words.txt"
            
            if not os.path.isfile(userInputFilePath):
                raise FileNotFoundError("File not found.")

            break

        except Exception as e:
            print(e)

    return userInputFilePath


def getVowelCount(file_path: str) -> Dict[str, int]:
    vowels: Dict[str, int] = { "a" : 0, "e" : 0, "i" : 0, "o" : 0, "u" : 0 }
    with open(file_path) as file:
        for line in file:
            word = line.strip()
            vowels['a'] += word.count("a")
            vowels['e'] += word.count("e")
            vowels['i'] += word.count("i")
            vowels['o'] += word.count("o")
            vowels['u'] += word.count("u")
    return vowels

def main() -> None:
    userFilePath: str = getUserFilePath()
    vowelCount: Dict[str, int] = getVowelCount(userFilePath)
    print(f"a: {vowelCount['a']}")
    print(f"e: {vowelCount['e']}")
    print(f"i: {vowelCount['i']}")
    print(f"o: {vowelCount['o']}")
    print(f"u: {vowelCount['u']}")

if __name__ == '__main__':
    main()