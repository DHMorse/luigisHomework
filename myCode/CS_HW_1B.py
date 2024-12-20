def count(value1: int, value2: int) -> None:
    value1: int = -1
    value2: int = 0
    while value1 < 999:
        value1 += 2
        value2 += value1
    print(value2)

def main() -> None:
    count(-1, 0)

if __name__ == '__main__':
    main()