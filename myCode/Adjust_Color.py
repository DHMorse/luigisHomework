# Adjust_Color.py

def adjustColor(filename: str = "myCode/Sailboat.raw") -> bytearray:
    with open(filename, "rb") as rawFile:
        output: bytearray = bytearray()
        byte: int = 1
        while byte:
            byte: bytes = rawFile.read(2)
            output.extend(byte)
            byte: bytes = rawFile.read(1)
            if byte:
                num: int = int(byte[0] * 1.1)
                if num > 255:
                    num: int = 255
                output.append(num)
    return output

def writeNewFile(output: bytearray, filename: str = "myCode/Sailboat1.raw") -> None:
    with open(filename, "wb") as newFile:
        newFile.write(output)

def main() -> None:
    output: bytearray = adjustColor()
    writeNewFile(output)

if __name__ == "__main__":
    main()