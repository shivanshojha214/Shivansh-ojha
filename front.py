from tkinter import*
from PIL  import Image,ImageTk
from main import openCamera



window=Tk()
window.title("The Eagle Eye")
window.iconphoto(False,PhotoImage(file='mn.png'))
window.geometry('1080x600')

def closeApp():
    window.destroy()

#main frame
mainframe = Frame(window,bd=2)

label_title = Label(mainframe,text = "The Eagle Eye", font=('Helvitica',40,'bold'),compound='center')
label_title.grid(row = 0,column=2, sticky= NSEW)

icon_1=Image.open("mn.png")
icon_1 = icon_1.resize((50,50),Image.ANTIALIAS)
icon_1=ImageTk.PhotoImage(icon_1)
Label_icon_1=Label(mainframe,image=icon_1)
Label_icon_1.grid(row=0,pady=(1,1),column=0, sticky= NSEW)

icon_spy=Image.open("icons/spa.png")
icon_spy=icon_spy.resize((180,180),Image.ANTIALIAS)
icon_spy=ImageTk.PhotoImage(icon_spy)
Label_icon_spay=Label(mainframe,image=icon_spy)
Label_icon_spay.grid(row=4,pady=(5,10),column=2)

#btn recording
btn_image=Image.open("icons/recording.png")
btn_image=btn_image.resize((50,50),Image.ANTIALIAS)
btn_image=ImageTk.PhotoImage(btn_image)
label_btn_image=Label(mainframe,image=btn_image)
# label_btn_image.grid(row = 5, pady=(5,5), column=5 )

btn=Button(mainframe,text="VideoRecord",font=('Helvitica',25,'bold'),height=90,width=270,fg='orange',image=btn_image,compound='left',command= openCamera)
btn.grid(row=3,pady=(10,10),column=2)

# exit btn
btn_image1=Image.open("icons/exit.png")
btn_image1=btn_image1.resize((50,50),Image.ANTIALIAS)
btn_image1=ImageTk.PhotoImage(btn_image1)

btn_exit=Button(mainframe,text="Exit",font=('Helvitica',25,'bold'),height=90,width=270,fg='orange',image=btn_image1,compound='left', command= closeApp )
btn_exit.grid(row=5,pady=(20,10),column=2)

mainframe.pack()

window.mainloop()


