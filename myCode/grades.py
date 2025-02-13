def getUserInputGrade() -> int:
    while True:
        try:
            userInputGradeString: str = input("Type your grade: ").strip()
            
            if userInputGradeString.isnumeric():
                userInputGrade: int = int(userInputGradeString)
                if 0 <= userInputGrade <= 100:
                    break
                else:
                    print("Grade must be between 0 and 100")
            else:
                print("Grade must be a number")

        except Exception as e:
            print(e)

    return userInputGrade


def main() -> None:
    grade: int = getUserInputGrade()
    
    if grade >= 90:
        print("You made an A")
    elif grade >= 80:
        print("You made an B")
    elif grade >= 70:
        print("You made an C")
    else:
        print("You failed")

if __name__ == "__main__":
    main()