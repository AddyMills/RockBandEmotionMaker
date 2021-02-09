import sys
from a3process import a3_notes_to_text, a3_text_to_notes

sys.argv=["Main"]
from Tkinter import Tk, Frame, Button, Label, HORIZONTAL

import ttk

def main():
    form = Tk()
    form.wm_title("Audrey 3.0")
    form.minsize(height=148, width=74)

    Label(form, text="Use velocity for the visme parameters.").grid(row=0, column=0, pady=5, columnspan=2)
    Label(form, text="Use channel as a multiplier for velocty to reach 255.").grid(row=1, column=0, pady=5, columnspan=2)

    ttk.Separator(form, orient="horizontal").grid(row=2, column=0, columnspan=2)

    btn_fromnotes = Button(form, text="Notes to Text",
            width=22, command=a3_notes_to_text)
    btn_fromnotes.grid(row=3, column=0, padx=3, pady=3, sticky="w")

    btn_fromtext = Button(form, text="Text to Notes",
            width=22, command=a3_text_to_notes)
    btn_fromtext.grid(row=3, column=1, padx=3, pady=3, sticky="w")

    form.mainloop()

if __name__ == "__main__":
    main()
    
