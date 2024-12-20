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

def getNumTimesWordAppears(file_path: str, word: str) -> int:
    word_count: int = 0
    with open(file_path) as file:
        for line in file:
            word_count += line.count(word)
    return word_count

def main() -> None:
    userFilePath: str = getUserFilePath()
    numTimesPeople: int = getNumTimesWordAppears(userFilePath, "people")
    numTimesCongress: int = getNumTimesWordAppears(userFilePath, "congress")
    print(f"The word \"People\" appears: {numTimesPeople} times.")
    print(f"The word \"Congress\" appears: {numTimesCongress} times.")

    # or since we never use the varibles again we could just print the return values
    #print(f"The word \"People\" appears: {getNumTimesWordAppears(userFilePath, 'people')} times.")
    #print(f"The word \"Congress\" appears: {getNumTimesWordAppears(userFilePath, 'congress')} times.")

if __name__ == '__main__':
    main()