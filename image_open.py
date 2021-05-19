from tkinter import *
import db as db
# loading Python Imaging Library
from PIL import ImageTk, Image
import  shutil as util
import os
# To get the dialog box to open when required
from tkinter import filedialog
import photos as ph
import video as video
import live as live

currentId = 0
db.getHistory()
def onclick(args):
    global currentId
    if args ==7:
        print("next")
        if currentId < len(db.result):
            currentId = currentId + 1
            show_img(db.result[currentId][2])

    if args ==2:
        print(" previous")
        if currentId !=0:
            currentId = currentId - 1
            show_img(db.result[currentId][2])
    if args ==3:
        print("photos")
        ph.start('pic2.jpg')
    if args ==4:
        print("video")
        video.start()
    if args ==5:
        print("live")
        live.start()



# Create a windoe
root = Tk()

# Set Title as Image Loader
root.title("Image Loader")

# Set the resolution of window


# Allow Window to be resizable

root.resizable(width = True, height = True)

def show_img(loc):
    img = Image.open(loc)
    # img = Image.open('./outputs/' + os.path.basename(x))
    img = img.resize((400, 400), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    print(img)

    # create a label
    panel = Label(root, image=img)

    # set the image as img
    panel.image = img
    panel.grid(row=2)
def open_img():
    global currentId
    currentId = 0
    # Select the Imagename from a folder
    x = openfn()
    util.copy(x, './images/')
    print(os.path.basename(x))
    ph.start('./images/'+os.path.basename(x))
    # opens the image
    db.insertImage('./outputs/'+os.path.basename(x))
    currentId = len(db.result) - 1
    show_img(db.result[currentId][2])

def openfn():
    filename=filedialog.askopenfilename(title='open')
    return filename


# Create a button and place it into the window using grid layout
btn = Button(root, text ='open image', command = open_img).grid(row=1,columnspan=4)

btn2 =Button(root,text="next ",command=lambda:onclick(2)).grid(row=3,columnspan=4)
btn3= Button(root,text="Photos",command=lambda:onclick(3)).grid(row=4,columnspan=4)
btn4= Button(root,text="live",command=lambda:onclick(5)).grid(row=5,columnspan=4)
btn5= Button(root,text="video",command=lambda:onclick(4)).grid(row=6,columnspan=4)





root.mainloop()





