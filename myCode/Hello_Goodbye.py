# Hellow_Goodbye.py

from tkinter import Tk, Button

def printHello() -> None:
    print("Hello")

def printGoodbyeAndQuit():
    print("goodbye")
    quit()

def main() -> None:
    root: Tk = Tk()
    
    helloButton: Button = Button(root, text="Hello", command=printHello)
    helloButton.pack()
    
    goodbyeButton: Button = Button(root, text="Goodbye", command=printGoodbyeAndQuit)
    goodbyeButton.pack()
    
    root.mainloop()

if __name__ == "__main__":
    main()