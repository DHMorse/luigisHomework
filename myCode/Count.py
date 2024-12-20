def countFromStartNumToEndNum(startNum: int, endNum: int) -> None:
    for i in range(startNum, endNum + 1):
        print(i)

def main() -> None:
    print("Count from 1 to 10")
    countFromStartNumToEndNum(1, 10)
    print("The End")

if __name__ == '__main__':
    main()