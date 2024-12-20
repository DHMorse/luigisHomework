# File_Search.py

from tkinter import *
from tkinter.scrolledtext import *
from tkinter.filedialog import *
root = Tk()

class SearchableFile:
    fileName = ""
    lines = []

    def getFileName(self):
        return self.fileName

    def setFileName(self, f):
        self.fileName = f

    def readFile(self):
        if self.fileName == "":
            print("File name not specified")
        else:
            self.lines = []
            print("reading " + self.fileName)
            file = open(self.fileName)
            for line in file:
                self.lines.append(line)

    def getContent(self):
        s = ""
        num = 0
        for line in self.lines:
            num = num + 1
            s = s + str(num).rjust(3, '0') + "   " + line
        return s

    def search(self, s):
        result = ""
        num = 0
        for line in self.lines:
            num = num + 1
            if s in line:
                result = result + str(num).rjust(3, '0') + "   " + line
        return result

sf = SearchableFile()
svFileName = StringVar()
svSearchText = StringVar()

def chooseFile():
    f = askopenfilename()
    svFileName.set(f)
    sf.setFileName(f)

def openFile():
    sf.readFile()
    s = sf.getContent()
    content.delete(1.0, END)
    content.insert(INSERT, s)

def searchFile():
    s = svSearchText.get()
    print("Search Text:", s)
    r = sf.search(s)
    results.delete(1.0, END)
    results.insert(INSERT, r)

# Create Frame 1 and the controls to go in it
frame1 = Frame(root, width = 200, height = 600, bg="#FFEEDD")
txtFile = Entry(frame1, width=20, textvariable=svFileName)
btnBrowse = Button(frame1, width=10, text="Browse", command=chooseFile)
btnOpen = Button(frame1, width=10, text="Open", command=openFile)

txtFile.grid(row=0, column=0)
btnBrowse.grid(row=1, column=0)
btnOpen.grid(row=2, column=0)

# Create Frame 2 and the controls to go in it
frame2 = Frame(root, width=200, height=200, bg="#DDFFEE")
txtSearch = Entry(frame2, width=20,textvariable=svSearchText)
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

mainloop()