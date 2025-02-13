# Feed_the_Sprats.py

from tkinter import Tk, StringVar, Label, Button
from Person import Person

def main() -> None:
    root: Tk = Tk()
    
    jackStringVar: StringVar = StringVar()
    joanStringVar: StringVar = StringVar()

    jackPerson: Person = Person(name="Jack", height=70, weight=150, mealSize=1)
    joanPerson: Person = Person(name="Joan", height=63, weight=240, mealSize=3)

    def feedPersonButtonClickFunc(stringVar: StringVar, person: Person):
        person.eat()
        stringVar.set(f'{person.name}: {str(person.weight)}')

    jackLable: Label = Label(root, textvariable=jackStringVar,width=10,height=3)
    joanLable: Label = Label(root, textvariable=joanStringVar,width=10,height=3)

    feedJackButton: Button = Button(root, text="Feed Jack", command=lambda: feedPersonButtonClickFunc(jackStringVar, jackPerson))
    feedJoanButton: Button = Button(root, text="Feed Joan", command=lambda: feedPersonButtonClickFunc(joanStringVar, joanPerson))

    jackLable.grid(row=0, column=0)
    joanLable.grid(row=0, column=1)

    feedJackButton.grid(row=1, column=0)
    feedJoanButton.grid(row=1, column=1)
    
    root.mainloop()

if __name__ == "__main__":
    main()