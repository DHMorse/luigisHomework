from typing import List

def makeCudedList(numOfCubes: int) -> List[int]:
    cubed_list: List[int] = []
    for cubed in range(1, numOfCubes + 1):
        cubed **= 3
        cubed_list.append(cubed)
    return cubed_list


def main() -> None:
    print("Perfect Cubes")
    cubedList: List[int] = makeCudedList(50)
    for index, cube in enumerate(cubedList):
        print(f'{index + 1} cubed = {cube}')

if __name__ == '__main__':
    main()