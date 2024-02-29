from tkinter import*

click=0
def btn_click():
    click=+1
    print("Button Clicked", click)


window = Tk()

btn = Button(window, text="click me!",
             command=btn_click)
btn.pack()

window.mainloop()
