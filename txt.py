import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
window = tk.Tk()
window.title("Codingal's Text Editor")
window.geometry("600x500")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)
def open_file():
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
        input_file.close()
    window(f"Codingal's Text Editor - {filepath}")
def save_file():
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)
    window.title(f"Codingal's Text Editor - {filepath}")
txt.edit = Text(window)
fr_btns = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_open = tk.Button(fr_btns, text="open", command=open_file)
btn_save = tk.Button(fr_btns, text="Save as....", command=save_file)
btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)
fr_btns.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky=nsew)
window.mainloop()   