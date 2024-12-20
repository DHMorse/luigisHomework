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


# Count the total number of t's in each word
def number_of_t(file_path: str) -> int:
    t_count: int = 0
    with open(file_path) as file:
        for line in file:
            word = line.strip()
            t_count += word.count("t")
    return t_count

def main() -> None:
    userFilePath: str = getUserFilePath()
    t_count: int = number_of_t(userFilePath)
    print(f"Total: {t_count}")

if __name__ == '__main__':
    main()