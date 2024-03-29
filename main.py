# Icon by Freepik from www.flaticon.com
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox

global open_file
global is_old
open_file = None
is_old = False

root = Tk()
root.geometry("900x450")
root.title("wrote")
icon = PhotoImage(file = 'notes.png')
root.iconphoto(True, icon)

def newNote():
	global open_file
	global is_old

	text.delete(1.0, END)
	root.title("wrote")
	open_file = None
	is_old = False

def saveNote():
	global open_file
	global is_old

	if is_old:
		with open(open_file, "w") as file:
			file.write(text.get(1.0, "end-1c"))
	else:
		f = fd.asksaveasfilename(filetypes = (("Text files", "*.txt"), ("All files", "*.*")))
		with open(f, "w") as file:
			file.write(text.get(1.0, "end-1c"))
		root.title(f)

def openNote():
	global open_file
	global is_old

	f = fd.askopenfilename(filetypes = (("Text files", "*.txt"), ("All files", "*.*")))
	text.delete(1.0, END)

	with open(f, "r") as file:
		text.insert(1.0, file.read())
	
	is_old = True
	open_file = f
	root.title(f)

def cut():
	text.event_generate(("<<Cut>>"))

def copy():
	text.event_generate(("<<Copy>>"))

def paste():
	text.event_generate(("<<Paste>>"))

def aboutApp():
	messagebox.showinfo("About", "Made with love by Rishav Mitra")

menubar = Menu(root)
# File menu Starts
filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label = "New", command = newNote)
filemenu.add_command(label = "Save", command = saveNote)
filemenu.add_command(label = "Open", command = openNote)
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = root.destroy)
menubar.add_cascade(label = "File", menu = filemenu)
# File menu Ends

# Edit menu Starts
editmenu = Menu(menubar, tearoff = 0)
editmenu.add_command(label = "Cut", command = cut)
editmenu.add_command(label = "Copy", command = copy)
editmenu.add_command(label = "Paste", command = paste)
menubar.add_cascade(label = "Edit", menu = editmenu)
# Edit menu Ends

# Help menu Starts
helpmenu = Menu(menubar, tearoff = 0)
helpmenu.add_command(label = "About", command = aboutApp)
menubar.add_cascade(label = "Help", menu = helpmenu)
# Help menu Ends

scroll = Scrollbar(root)
scroll.pack(side = RIGHT, fill = Y)

text = Text(root, yscrollcommand = scroll.set)
text.pack(fill = BOTH)
text.configure(font = ("Comic Sans MS", 20))
text.focus()

scroll.config(command = text.yview)

root.config(menu = menubar)
root.mainloop()
