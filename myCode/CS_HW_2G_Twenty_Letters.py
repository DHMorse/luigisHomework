import os
from typing import List

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

def getWordsLongerThan20Chars(file_path: str) -> List[str]:
    words: List[str] = []
    with open(file_path) as file:
        for line in file:
            word = line.strip()
            if len(word) >= 20:
                words.append(word)
    return words

def main() -> None:
    userFilePath: str = getUserFilePath()
    words: List[str] = getWordsLongerThan20Chars(userFilePath)
    words.sort()
    for word in words:
        print(word)
    print(f"Total: {len(words)}")

if __name__ == '__main__':
    main()