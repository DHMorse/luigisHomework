from typing import Tuple

def getUserLengths() -> Tuple[float, float, float]:
    while True:
        try:
            len1: float = float(input("Enter the first length of the triangle: "))
            len2: float = float(input("Enter the second length of the triangle: "))
            len3: float = float(input("Enter the third length of the triangle: "))
            if len1 <= 0 or len2 <= 0 or len3 <= 0:
                raise ValueError("Lengths must be greater than 0.")
            break
        except Exception as e:
            print(e)
    return (len1, len2, len3)

def isRight(len1: float, len2: float, len3: float, sidesTuple: Tuple[float, float, float] = None) -> bool:
    a, b, c = sorted([len1, len2, len3] if sidesTuple is None else sorted(sidesTuple))
    return (a**2 + b**2) == c**2

def main() -> None: 
    print("Right Triangle Checker")
    len1, len2, len3 = getUserLengths()
    if isRight(len1, len2, len3):
        print("That triangle is a Right Triangle!")
    else:
        print("That triangle is not a Right Triangle.")

if __name__ == '__main__':
    main()