from typing import Tuple

def getUserWidth() -> float:
    while True:
        try:
            width: float = float(input("Enter the width of the room in feet: "))
            if width <= 0:
                raise ValueError("Width must be greater than 0.")
            break
        except Exception as e:
            print(e)
    return width

def getUIserHeight() -> float:
    while True:
        try:
            height: float = float(input("Enter the height of the room in feet: "))
            if height <= 0:
                raise ValueError("Height must be greater than 0.")
            break
        except Exception as e:
            print(e)
    return height

def calculate_paint(width: float, height: float) -> Tuple[float, float]:
    return (width * height, (width * height) / 350)

def main() -> None:
    print("Paint Calculator")
    width: float = getUserWidth()
    height: float = getUIserHeight()
    area, gallons = calculate_paint(width, height)
    print(f"Area: {area} square feet")
    print(f"Gallons: {gallons}")

if __name__ == '__main__':
    main()