# File_Search.py

from tkinter import Tk, StringVar, Frame, Button, Entry, INSERT, END
from tkinter.scrolledtext import ScrolledText
from tkinter.filedialog import askopenfilename

class SearchableFile:
    fileName: str = ''
    lines: list[str] = []

    def getFileName(self: object) -> str:
        return self.fileName

    def setFileName(self: object, fileName: str) -> None:
        self.fileName = fileName

    def readFile(self: object) -> None:
        if self.fileName == '':
            print("File name not specified")
        else:
            self.lines: list = [str]
            print(f"reading {self.fileName}")
            with open(self.fileName) as file:
                for line in file:
                    self.lines.append(line)

    def getContent(self: object) -> str:
        string: str = ''
        counter: int = 0
        for line in self.lines:
            counter += 1
            string += str(counter).rjust(3, '0') + "   " + line
        return string

    def search(self: object, string: str) -> str:
        result: str = ''
        counter: int = 0
        for line in self.lines:
            counter += 1
            if string in line:
                result += str(counter).rjust(3, '0') + "   " + line
        return result

def main() -> None:
    root: Tk = Tk()

    searchableFileVar: SearchableFile = SearchableFile()
    stringVarFileName: StringVar = StringVar()
    stringVarSearchText: StringVar = StringVar()

    def chooseFile() -> None:
        file: str = askopenfilename()
        stringVarFileName.set(file)
        searchableFileVar.setFileName(file)

    def openFile() -> None:
        searchableFileVar.readFile()
        fileContent: str = searchableFileVar.getContent()
        content.delete(1.0, END)
        content.insert(INSERT, fileContent)

    def searchFile() -> None:
        fileContent = stringVarSearchText.get()
        print("Search Text:", fileContent)
        searchResults: str = searchableFileVar.search(fileContent)
        results.delete(1.0, END)
        results.insert(INSERT, searchResults)

    # Create Frame 1 and the controls to go in it
    frame1 = Frame(root, width = 200, height = 600, bg="#FFEEDD")
    txtFile = Entry(frame1, width=20, textvariable=stringVarFileName)
    btnBrowse = Button(frame1, width=10, text="Browse", command=chooseFile)
    btnOpen = Button(frame1, width=10, text="Open", command=openFile)

    txtFile.grid(row=0, column=0)
    btnBrowse.grid(row=1, column=0)
    btnOpen.grid(row=2, column=0)

    # Create Frame 2 and the controls to go in it
    frame2 = Frame(root, width=200, height=200, bg="#DDFFEE")
    txtSearch = Entry(frame2, width=20,textvariable=stringVarSearchText)
    btnSearch = Button(frame2, width=10, text="Search", command=searchFile)

    txtSearch.grid(row=0, column=0)
    btnSearch.grid(row=1, column=0)

    # Create two ScrolledText objects to display the info
    content = ScrolledText(root, width=60, height=20, bg="#FFFFDD")
    results = ScrolledText(root, width=60, height=10, bg="#DDEEFF")

    # Put everything into the grid
    frame1.grid(row=0, column=0, sticky="NS")
    frame2.grid(row=1, column=0, sticky="NS")
    content.grid(row=0, column=1)
    results.grid(row=1,column=1)
    root.mainloop()

if __name__ == "__main__":
    main()