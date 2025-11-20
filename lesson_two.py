import tkinter as tk

#create window
win = tk.Tk()

#function

#create a "printtext" function for print words in the terminal 
def printtext():
    print(entry.get())

#create a "inserttext" function for insert latest words and the back of the current words
def inserttext():
    entry.insert(tk.END, entry2.get())
    
#create a "deletetext" function for words deletion
def deletetext():
    entry.delete(0,tk.END)

#image upload
p1 = tk.PhotoImage(file = "elements\download.png")

#setting of window
win.title("Personal details")
win.iconphoto(False,p1)
win.geometry("300x200")

#main script
label1 = tk.Label(text="Name")
entry = tk.Entry()
btn = tk.Button(text = 'Print', command = printtext)
entry2 = tk.Entry()
btn2 = tk.Button(text = 'Insert', command = inserttext)
btn3 = tk.Button(text = 'Delete', command = deletetext)
btn4 = tk.Button(text = 'Close', command = win.destroy)

#add widget to window
label1.pack()
entry.pack()
btn.pack()
entry2.pack()
btn2.pack()
btn3.pack()
btn4.pack()

#looping of window
win.mainloop()