import os

# Find all the words with a double o
# display each word and keep a running total

def find_double_o_words(file_path: str) -> int:
    double_o_count = 0
    with open(file_path) as file:
        for line in file:
            word = line.strip()
            if word.find("oo") >=0:
                print(word)
                double_o_count += 1
    return double_o_count 

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


def main() -> None:
    userFilePath: str = getUserFilePath()
    double_o_count: int = find_double_o_words(userFilePath)
    print(f"Total: {double_o_count}")

if __name__ == '__main__':
    main()