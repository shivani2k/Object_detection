import tkinter as tk
from PIL import ImageTk,Image
from tkinter.ttk import *
from tkinter.filedialog import askopenfile
import photos as ph
import video as video
import live as live
def onclick(args):
    if args ==1:
        print("next")

    if args ==2:
        print(" previous")
    if args ==3:
        print("upload")
        ph.start('sagar3.jpeg')
    if args ==4:
        print("photos")
        video.start()
    if args ==5:
        print("live")
        live.start()
    if args ==6:
        print("video")
def open_file():
    file=askopenfile(mode='r',fieldtypes=[('python Files','*py'),("Text file","*.txt*"),("all files","*.*")])
    if file is not None:
        content =file.read()
        print(content)


root = tk.Tk()
root.title("gui button ")

btn1 = tk.Button(root, text="next",command=lambda:onclick(1))
btn2 =tk.Button(root,text="previous ",command=lambda:onclick(2))
btn3= tk.Button(root,text="Photos",command=lambda:onclick(3))
btn4= tk.Button(root,text="live",command=lambda:onclick(4))
btn5= tk.Button(root,text="video",command=lambda:onclick(5))
btn6 =tk.Button(root,text='open',command=lambda:open_file() )
btn6.pack()
btn1.pack()
btn2.pack()
btn3.pack()
btn4.pack()
btn5.pack()
root.mainloop()



