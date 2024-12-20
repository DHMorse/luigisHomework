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


def count_lines(file_path: str) -> int:
    lines: int = 0
    with open(file_path) as file:
        for line in file:
            lines += 1
    return lines


def main() -> None:
    userFilePath: str = getUserFilePath()
    lineCount: int = count_lines(userFilePath)
    print(f"Total: {lineCount}")

if __name__ == '__main__':
    main()