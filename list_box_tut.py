import tkinter as tk


def show_menu():
    root = tk.Tk()
    lvar = tk.StringVar()
    lvar.set(["1", "2", "3"])
    lb = tk.Listbox(root, listvariable=lvar)
    lb.pack()
    root.mainloop()



if __name__ == "__main__":
	show_menu()