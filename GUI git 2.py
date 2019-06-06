from tkinter import*
import tempfile
import io
import win32api
import win32print

x = 0

list = []

TP = 0

def r1():
    print("Ordering Margharita \n")
    list.append("Margharita")
    global x
    x = x + 1
    global TP
    TP = TP + 90

def r2():
    print("Ordering Peppy Paneer Pizza \n")
    list.append("Peppy Paneer Pizza")
    global x
    x = x + 1
    global TP
    TP = TP + 110
    
def r3():
    print("Ordering Country Feast \n")
    list.append("Country Feast")
    global x
    x = x + 1
    global TP
    TP = TP + 120
    
def r4():
    print("Ordering Cheese Burger \n")
    list.append("Cheese Burger")
    global x
    x = x + 1
    global TP
    TP = TP + 25

def r5():
    print("Ordering Potato Patty \n")
    list.append("Potato Patty")
    global x
    x = x + 1
    global TP
    TP = TP + 20
    
def r6():
    print("Ordering Tikki \n")
    list.append("Tikki")
    global x
    x = x + 1
    global TP
    TP = TP + 7

def r7():
    print("Ordering Pani Puri \n")
    list.append("Pani Puri")
    global x
    x = x + 1
    global TP
    TP = TP + 12

def r8():
    print("Ordering Momos \n")
    list.append("Momos")
    global x
    x = x + 1
    global TP
    TP = TP + 20

def r9():
    print("Ordering Fruit Salad \n")
    list.append("Fruit Salad")
    global x
    x = x + 1
    global TP
    TP = TP + 50

def done():
    print("Thank you for ordering \n"+
          "|||||||||||||| \n" +
          "|    BILL    | \n"+
          "|||||||||||||| \n"+
          "No. of Items = " + str(x) +
          "\n Name of Dishes = " + str(list) +
          "\n Total Cost = ₹" + str (TP))

    filename = tempfile.mktemp (".txt")
    with io.open (filename, "w", encoding="utf-8") as b:
        b.write ("Names of Dishes" + str(list) + "\nTotal items = " + str(x) + "\nTotal cost = ₹ " + str(TP))
    win32api.ShellExecute (
      0,
      "printto",
      filename,
      '"%s"' % win32print.GetDefaultPrinter (),
      ".",
      0
    )   
          
        
root = Tk()
root.geometry('300x400')
root.configure(background = '#ffd268')

l = Label(root, text="Welcome to Nawabi Shaq!", bg='#ffa5dd')
l.pack()          
    
b1 = Button(root, text = "Margharita", command=r1, bg='#ff8668')
b1.pack()

b2 = Button(root, text = "Peppy Paneer Pizza", command=r2, bg='#ff8668')
b2.pack()

b3 = Button(root, text = "Country Feast", command=r3, bg='#ff8668')
b3.pack()

b4 = Button(root, text = "Cheese Burger", command=r4, bg='#a5ddff')
b4.pack()

b5 = Button(root, text = "Potato Patty", command=r5, bg='#a5ddff')
b5.pack()

b6 = Button(root, text = "Tikki", command=r6, bg='#a5ddff')
b6.pack()

b7 = Button(root, text = "Pani Puri", command=r7, bg='#ddffa5')
b7.pack()

b8 = Button(root, text = "Momos", command=r8, bg='#ddffa5') 
b8.pack()

b9 = Button(root, text = "Fruit Salad", command=r9, bg='#ddffa5')
b9.pack()
        
f = Button(root, text ="Done", command = done, bg='#ffa5dd')
f.pack()

root.mainloop()


