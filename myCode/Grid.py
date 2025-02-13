# Grid.py

from tkinter import Tk, StringVar, Label, Button

def main() -> None:
    root = Tk()
    
    stringVarA = StringVar()
    stringVarB = StringVar()

    stringVarA.set("1")
    stringVarB.set("2")

    def buttonClick(stringVar: StringVar, letter: str) -> None:
        stringVar.set(letter)

    labelA = Label(root, textvariable=stringVarA)
    labelB = Label(root, textvariable=stringVarB)
    
    buttonA = Button(root, text="Button 1", command=lambda: buttonClick(stringVarA, "A"))
    buttonB = Button(root, text="Button 2", command=lambda: buttonClick(stringVarB, "B"))

    labelA.grid(row=0, column=0)
    labelB.grid(row=0, column=1)
    
    buttonA.grid(row=1, column=0)
    buttonB.grid(row=1, column=1)
    
    root.mainloop()

if __name__ == "__main__":
    main()