from time import sleep
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image

def fetchData():
    pbrun.configure(style="red.Horizontal.TProgressbar")
    pbrun.step(50)
    sleep(1)
    pbrun.configure(style="green.Horizontal.TProgressbar")
    pbrun.step(100)
    sleep(1)
    root.after(20, fetchData)

root = Tk()
root.title("Derpys Moon Mission")
root.geometry("1920x1080")
bg = PhotoImage(file="bg.png")
canvas1 = Canvas(root)
canvas1.pack(fill="both", expand=True)
canvas1.create_image(0, 0, image=bg,anchor="nw")

pagetitel = Label(canvas1, text="Mission Status",fg="orange",bg="black",font=("LCARS GTJ2 Condensed",30))
pagetitel.place( x= 380, y = 15,anchor = 'nw')

titel = Label(canvas1, text="Derpyfest 2024",fg="orange",bg="black",font=("LCARS GTJ2 Condensed",50))
titel.place( x=1350 , y = 10,anchor = 'nw')

menu1 = Label(canvas1, text="Crewnumber",fg="black",bg="#cd6562",font=("LCARS GTJ2 Condensed",35))
menu1.place( x=155 , y = 425,anchor = 'center')

menu2 = Label(canvas1, text="Missiontime",fg="black",bg="#9b9bff",font=("LCARS GTJ2 Condensed",35))
menu2.place( x=155 , y = 530,anchor = 'center')

menu3 = Label(canvas1, text="",fg="black",bg="#ffd09c",font=("LCARS GTJ2 Condensed",35))
menu3.place( x=155 , y = 635,anchor = 'center')

menu4 = Label(canvas1, text="Hydration",fg="black",bg="#9c99ce",font=("LCARS GTJ2 Condensed",35))
menu4.place( x=155 , y = 740,anchor = 'center')

menu5 = Label(canvas1, text="Status",fg="black",bg="#ff9a00",font=("LCARS GTJ2 Condensed",35))
menu5.place( x=155 , y = 845,anchor = 'center')


line1 = Label(canvas1, text="Guests: 50, VIP: 10, Volunteer: 15",fg="orange",bg="black",font=("LCARS GTJ2 Condensed",35))
line1.place( x=350 , y = 425,anchor = 'w')

s = ttk.Style()
s.theme_use('clam')
s.configure("yellow.Horizontal.TProgressbar", foreground='yellow', background='yellow')
s.configure("red.Horizontal.TProgressbar", foreground='red', background='red')
s.configure("green.Horizontal.TProgressbar", foreground='green', background='green')


# set maximum to overall con hours
pbrun = ttk.Progressbar(maximum=100,style="red.Horizontal.TProgressbar")
pbrun.place(x=350, y=535, width=1000, height=100,anchor='w')
#this sets status of bar
pbrun.step(30)

hours = Label(canvas1, text="Left: 10H",fg="orange",bg="black",font=("LCARS GTJ2 Condensed",35))
hours.place( x=1360 , y = 530,anchor = 'w')

# set maximum to overall con hours
pbhydration = ttk.Progressbar(maximum=100,style="red.Horizontal.TProgressbar")
pbhydration.place(x=350, y=750, width=1000, height=100,anchor='w')
#this sets status of bar
pbhydration.step(30)

hydration = Label(canvas1, text="100%",fg="orange",bg="black",font=("LCARS GTJ2 Condensed",35))
hydration.place( x=1360 , y = 740,anchor = 'w')

root.after(20, fetchData)
root.mainloop()

