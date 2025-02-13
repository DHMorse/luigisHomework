# HW_4A_Rectangle_Loop
# Luke Norvell

from tkinter import Canvas

def main() -> None:
    rectangleCanvas: Canvas = Canvas(width=800, height=600, bg="White")

    # Caculate space and stuff
    totalRectWidth: int = 20 * 12
    remainingSpace: int = 800 - totalRectWidth
    gap: int | float = remainingSpace / (12 + 1)

    for i in range(12):
        xPos = (i + 1) * gap + i * 20
        rectangleCanvas.create_rectangle(xPos, 150, xPos + 20, 250, outline="Blue", width=2,fill="Grey",activefill="Red")

    rectangleCanvas.pack()
    rectangleCanvas.mainloop()

if __name__ == "__main__":
    main()