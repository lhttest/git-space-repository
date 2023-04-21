import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

class App:
    def __init__(self, master):
        self.master = master
        master.title("Text Editor")
        master.geometry("500x300")

        self.text = tk.Text(master)
        self.text.pack(expand=True, fill="both")

        menu = tk.Menu(master)
        master.config(menu=menu)

        file_menu = tk.Menu(menu)
        menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Open", command=self.openFile)
        file_menu.add_command(label="Save", command=self.saveFile)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=master.quit)

        edit_menu = tk.Menu(menu)
        menu.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Copy", command=self.copyText)
        edit_menu.add_command(label="Cut", command=self.cutText)
        edit_menu.add_command(label="Paste", command=self.pasteText)

    def openFile(self):
        filename = filedialog.askopenfilename(defaultextension=".txt", filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
        if filename:
            with open(filename, "r") as f:
                text = f.read()
                self.text.delete("1.0", tk.END)
                self.text.insert(tk.END, text)

    def saveFile(self):
        filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
        if filename:
            with open(filename, "w") as f:
                text = self.text.get("1.0", tk.END)
                f.write(text)

    def copyText(self):
        selected_text = self.text.selection_get()
        self.master.clipboard_clear()
        self.master.clipboard_append(selected_text)

    def cutText(self):
        selected_text = self.text.selection_get()
        self.text.delete(tk.SEL_FIRST, tk.SEL_LAST)
        self.master.clipboard_clear()
        self.master.clipboard_append(selected_text)

    def pasteText(self):
        text = self.master.clipboard_get()
        self.text.insert(tk.INSERT, text)

root = tk.Tk()
app = App(root)
root.mainloop()