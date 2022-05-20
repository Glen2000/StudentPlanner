from tkinter import *
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file():
    """ Open file to edit """
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete("1.0", tk.END)
    with open(filepath, mode="r", encoding="utf-8") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Simple Text Editor - {filepath}")

def save_file():
    """Save current file as new file."""
    filepath = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, mode="w", encoding="utf-8") as output_file:
        text = txt_edit.get("1.0", tk.END)
        output_file.write(text)
    window.title(f"Simple Text Editor - {filepath}")

window = tk.Tk()
window.title("Simple Text Editor")
#window.attributes("-fullscreen", True)
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)


def RoomLocation():
    window.destroy()
    import RoomLocations

def Inbox():
    window.destroy()
    import Inbox

def weatherPage():
    window.destroy()
    import weatherAPI

def annoucements():
    window.destroy()
    import googleClassroom

def grades():
    window.destroy()
    import Grades

def textEdit():
    window.destroy()
    import textedit

def appointments():
    window.destroy()
    import Appointments

txt_edit = tk.Text(window)
frm_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_open = tk.Button(frm_buttons, text="Open", command=open_file)
btn_save = tk.Button(frm_buttons, text="Save As...", command=save_file)
btn_locations = tk.Button(frm_buttons, text="Room Locations", command=RoomLocation)
btn_inbox = tk.Button(frm_buttons, text="Inbox", command=Inbox)
btn_weather = tk.Button(frm_buttons, text="Weather", command=weatherPage)
btn_announcement = tk.Button(frm_buttons, text="Announcements", command=annoucements)
btn_appointments = tk.Button(frm_buttons, text="Appointments", command=appointments)
btn_grades = tk.Button(frm_buttons, text="Grades", command=grades)
btn_exit = tk.Button(frm_buttons, text="EXIT", command=window.destroy)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
btn_locations.grid(row=3, column=0, sticky="ew", padx=5, pady=5)
btn_inbox.grid(row=4, column=0, sticky="ew", padx=5, pady=5)
btn_weather.grid(row=5, column=0, sticky="ew", padx=5, pady=5)
btn_announcement.grid(row=6, column=0, sticky="ew", padx=5, pady=5)
btn_appointments.grid(row=7, column=0, sticky="ew", padx=5, pady=5)
btn_grades.grid(row=8, column=0, sticky="ew", padx=5, pady=5)
btn_exit.grid(row=9, column=0, sticky="ew", padx=5, pady=5)
frm_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()