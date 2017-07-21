from tkinter import *

root = Tk()

v = IntVar()

Label(root, 
      text="""Enter the type of compression you want do:""",
      justify = LEFT,
      padx = 20).pack()
Radiobutton(root, 
            text="Enter the filename as 'fortar.py' for archieving:",
            padx = 20, 
            variable=v, 
            value=1).pack(anchor=W)
Radiobutton(root, 
            text="Enter the filename as 'forbz2.py' for bz2 compression: ",
            padx = 20, 
            variable=v, 
            value=2).pack(anchor=W)
Radiobutton(root, 
            text="Enter the filename as 'forgzip.py' for gzip compression: ",
            padx = 20, 
            variable=v, 
            value=3).pack(anchor=W)
Radiobutton(root, 
            text="Enter the filename as 'forlzma.py' for lzma compression:",
            padx = 20, 
            variable=v, 
            value=4).pack(anchor=W)
Radiobutton(root, 
            text="Want to see user selection stats (y/n)?",
            padx = 20, 
            variable=v, 
            value=5).pack(anchor=W)

def seleted(root):
	if v==1:
		"do somthing"
	elif v==2:
		"ee"
	else:
		"rr"


mainloop()
