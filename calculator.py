from tkinter import *
import tkinter as tk

wind = tk.Tk()
wind.geometry('400x440')
wind.configure(background="skyblue")  # for background color
wind.title("CASIO")


Label(wind, text='CASIO CALCULATOR', font=('Helvetica', 15, 'bold'),
      bg='powderblue', relief='solid').pack()


Label(wind, text="CASIO VERSION 1.1", relief="solid",
      bg="pink").pack(side=BOTTOM)
Label(wind, text="================================================",
      bg="powderblue").pack()


# -----------------entry label--------------------
Label(wind, text="Input 1", font=('Helvetica', 10, 'bold'),
      bg="powderblue", relief="solid", width=18).place(x=40, y=80)

Label(wind, text="Input 2", font=('Helvetica', 10, 'bold'),
      bg="powderblue", relief="solid", width=18).place(x=40, y=130)

a = StringVar()
b = StringVar()
Entry(wind, text=a, width=25).place(x=200, y=80)
Entry(wind, text=b, width=25).place(x=200, y=130)

Label(wind, text='', font=('Helvetica', 10, 'bold'),
      bg="powderblue", relief="solid", width=18).place(x=200, y=180)


def model():
    try:  
    # testing datacreate
     x = float(a.get())
     y = float(b.get())
     z = x + y
    except:
          z='Invalid Input' 
    Label(wind, text=str(z), font=('Helvetica', 10, 'bold'),
          bg="powderblue", relief="solid", width=18).place(x=200, y=180)


Button(wind, text="+", bg='powderblue',
       width=18, command=model).place(x=40, y=180)


Label(wind, text='', font=('Helvetica', 10, 'bold'),
      bg="powderblue", relief="solid", width=18).place(x=200, y=230)


def model1():
    try:  
    # testing datacreate
     x = float(a.get())
     y = float(b.get())
     z = x - y
    except:
          z='Invalid Input'  

    Label(wind, text=str(z), font=('Helvetica', 10, 'bold'),
          bg="powderblue", relief="solid", width=18).place(x=200, y=230)


Button(wind, text="-", bg='powderblue',
       width=18, command=model1).place(x=40, y=230)


Label(wind, text='', font=('Helvetica', 10, 'bold'),
      bg="powderblue", relief="solid", width=18).place(x=200, y=280)


def model2():
    try:  
    # testing datacreate
     x = float(a.get())
     y = float(b.get())
     z = x * y
    except:
          z='Invalid Input'

    Label(wind, text=str(z), font=('Helvetica', 10, 'bold'),
          bg="powderblue", relief="solid", width=18).place(x=200, y=280)


Button(wind, text="*", bg='powderblue',
       width=18, command=model2).place(x=40, y=280)


Label(wind, text='', font=('Helvetica', 10, 'bold'),
      bg="powderblue", relief="solid", width=18).place(x=200, y=330)


def model3():
    try:  
    # testing datacreate
     x = float(a.get())
     y = float(b.get())
     if y == 0:
        try:
            z = x / y
        except:
            z = "can't divide by zero"
     else:
        z = x / y
    except:
          z='Invalid Input'

    Label(wind, text=str(z), font=('Helvetica', 10, 'bold'),
          bg="powderblue", relief="solid", width=18).place(x=200, y=330)


Button(wind, text="/", bg='powderblue',
       width=18, command=model3).place(x=40, y=330)


def Exit():
    exit(0)


Button(wind, text="OFF", bg='powderblue',
       width=9, command=Exit).place(x=40, y=380)


def clear():
    Label(wind, text=" "*30, font=('Helvetica', 10, 'bold'),
          bg="powderblue", relief="solid", width=18).place(x=200, y=180)
    Label(wind, text=" "*30, font=('Helvetica', 10, 'bold'),
          bg="powderblue", relief="solid", width=18).place(x=200, y=230)
    Label(wind, text=" "*30, font=('Helvetica', 10, 'bold'),
          bg="powderblue", relief="solid", width=18).place(x=200, y=280)
    Label(wind, text=" "*30, font=('Helvetica', 10, 'bold'),
          bg="powderblue", relief="solid", width=18).place(x=200, y=330)


Button(wind, text="Clear", bg='powderblue', width=9,
       command=clear).place(x=200, y=380)


Button(wind, text="Reset", bg='powderblue',
       width=9, command=clear).place(x=100, y=380)


def Devloper():
      root=tk.Tk()
      root.geometry('400x400')
      root.title('About Devloper Information')
      root.configure(background="skyblue")  # for background color

# -----------------entry label--------------------
      Label(root, text="Devloper", font=('Helvetica', 10, 'bold'),
      bg="pink", relief="solid", width=18).place(x=60, y=40)

      Label(root, text="Age", font=('Helvetica', 10, 'bold'),
      bg="pink", relief="solid", width=18).place(x=60, y=60)
      
# -----------------entry label--------------------
      Label(root, text="Institute", font=('Helvetica', 10, 'bold'),
      bg="pink", relief="solid", width=18).place(x=60, y=80)

      Label(root, text="Work as", font=('Helvetica', 10, 'bold'),
      bg='pink', relief="solid", width=18).place(x=60, y=100)
      
# -----------------entry label--------------------
      Label(root, text="Work On", font=('Helvetica', 10, 'bold'),
      bg="pink", relief="solid", width=18).place(x=60, y=120)

      Label(root, text="Date", font=('Helvetica', 10, 'bold'),
      bg="pink", relief="solid", width=18).place(x=60, y=140) 
      Label(root, text="Akash Kumar", font=('Helvetica', 10, 'bold'),
      bg="pink", relief="solid", width=18).place(x=200, y=40)

      Label(root, text="20", font=('Helvetica', 10, 'bold'),
      bg="pink", relief="solid", width=18).place(x=200,y=60)
# -----------------entry label--------------------
      Label(root, text="MIT", font=('Helvetica', 10, 'bold'),
      bg="pink", relief="solid", width=18).place(x=200, y=80)

      Label(root, text="Software Eng.", font=('Helvetica', 10, 'bold'),
      bg='pink', relief="solid", width=18).place(x=200, y=100)
      
# -----------------entry label--------------------
      Label(root, text="Machine Learning", font=('Helvetica', 10, 'bold'),
      bg="pink", relief="solid", width=18).place(x=200, y=120)

      Label(root, text="09/09/2020", font=('Helvetica', 10, 'bold'),
      bg="pink", relief="solid", width=18).place(x=200, y=140)


      def destroy():
            root.destroy()
      Button(root, text="Exit", bg='powderblue',
       width=9, command=destroy).place(x=150, y=200)
      root.resizable(0,0)
      root.mainloop()


Button(wind, text="Devloper", bg='powderblue', width=9,
       command=Devloper).place(x=270, y=380)


wind.resizable(0, 0)
wind.mainloop()
