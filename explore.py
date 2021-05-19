from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile
root =Tk()
def open_file():
    file = askopenfile(mode='r',filetypes=[('python Files','*.py'),("Text files","*.txt*"),("all files","*.*")])
    if file is not None:
        content = file.read()
        print(content)
btn = Button(root,text='open',command=lambda:open_file() )
btn.pack()
mainloop()