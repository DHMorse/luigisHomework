import math
from typing import Dict

def getUserRadius() -> float:
    while True:
        try:
            radius = float(input("Enter a floating point number for the radius of the circle: "))
            if radius <= 0:
                raise ValueError("Radius must be greater than 0.")
            break
        except Exception as e:
            print(e)
    return radius

def analyze_circle(radius: float) -> Dict[str, float]:
    return {
        "radius": radius,
        "diameter": radius * 2,
        "circumference": radius * 2 * math.pi,
        "area": radius ** 2 * math.pi
    }


def main() -> None:
    print("Circle Analyzer")
    userRadius = getUserRadius()
    cirlceData: dict = analyze_circle(userRadius)
    print("Circle Info:")
    print(f"Radius: {userRadius}")
    print(f"Diameter: {cirlceData['diameter']}")
    print(f"Circumference: {cirlceData['circumference']}")
    print(f"Area: {cirlceData['area']}")

if __name__ == '__main__':
    main()