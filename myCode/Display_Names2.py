from typing import List

NAMES: List[str] = ["Thorin", "Fili", "Kili", "Bifur", "Bofur", "Bombur", "Balin", "Dawlin", "Oin", "Gloin", "Ori", "Nori", "Dori"]

def printNames(names: List[str]) -> None:
    for name in names:
        print(name)

def main() -> None:
    printNames(NAMES)

if __name__ == '__main__':
    main()