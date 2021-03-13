import sys
from a3process import a3_notes_to_text, a3_text_to_notes
from vgreaper import get_all_track_names

sys.argv=["Main"]
from Tkinter import Tk, Frame, Button, Label, StringVar, OptionMenu, HORIZONTAL

import ttk

global form
global track_var

def execute_notes_to_text():
    global form
    global track_var

    track = track_var.get().lower()
    a3_notes_to_text(track)
    form.destroy()

def execute_text_to_notes():
    global form
    global track_var

    track = track_var.get().lower()
    a3_text_to_notes(track)
    form.destroy()

def main():
    global form
    global track_var

    form = Tk()
    form.wm_title("Audrey 3.0")
    form.minsize(height=148, width=74)

    Label(form, text="Use velocity for the visme parameters.").grid(row=0, column=0, pady=5, columnspan=2)
    Label(form, text="Use channel as a multiplier for velocty to reach 255.").grid(row=1, column=0, pady=5, columnspan=2)

    ttk.Separator(form, orient="horizontal").grid(row=2, column=0, columnspan=2)

    tracks = get_all_track_names()
    OPTIONS = [t for t in tracks if t.startswith("LIPSYNC")]

    track_var = StringVar(form)
    track_var.set(OPTIONS[0])

    trackOpt = apply(OptionMenu, (form, track_var) + tuple(OPTIONS))
    trackOpt.grid(row=3, column=0, columnspan=1, sticky="WE", pady=3)

    btn_fromnotes = Button(form, text="Notes to Text",
            width=22, command=execute_notes_to_text)
    btn_fromnotes.grid(row=4, column=0, padx=3, pady=3, sticky="w")

    btn_fromtext = Button(form, text="Text to Notes",
            width=22, command=execute_text_to_notes)
    btn_fromtext.grid(row=4, column=1, padx=3, pady=3, sticky="w")

    Label(form, text="This may take some time. Please be patient.").grid(row=5, column=0, pady=5, columnspan=2)

    form.mainloop()

if __name__ == "__main__":
    main()
    
