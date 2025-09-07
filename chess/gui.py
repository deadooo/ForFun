from tkinter import * 

gui = Tk()
gui.geometry("800x800")
gui.title("Your Life")

icon = PhotoImage(file='chess/gameasset/teto_icon.png')
gui.iconphoto(True, icon)
gui.config(background="Brown")

def startButtonClicked():
    myLabel = Label(gui, text="Cums")
    myLabel.pack()

startButton = Button(gui, text="Touch me now please!", command=startButtonClicked)
startButton.pack()

gui.mainloop()    

