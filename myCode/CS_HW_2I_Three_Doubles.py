import os

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

def hasThreeSetsOfDoubleLetters(word: str) -> bool:
    doubleLetterCount: int = 0
    for i in range(len(word) - 1):
        if word[i] == word[i + 1]:
            doubleLetterCount += 1
            i += 1
    return doubleLetterCount == 3

def countWordsWithThreeDoubleLetters(filePath: str) -> int:
    total: int = 0
    with open(filePath) as file:
        for line in file:
            word = line.strip()
            if hasThreeSetsOfDoubleLetters(word):
                print(word)
                total += 1
    return total

def main() -> None:
    userFilePath: str = getUserFilePath()
    numOfWordsWithThreeDoubleLetters: int = countWordsWithThreeDoubleLetters(userFilePath)
    print(f"Number of words found with three or more sets of double letters: {numOfWordsWithThreeDoubleLetters}")


if __name__ == '__main__':
    main()