from tkinter import *

def show_info():
    message_txt.delete(0.0, 'end')
    selected_rat = rat_entry.get()

    for label in magic_rats.grid_slaves():
        if int(label.grid_info()["row"]) == 6:
            label.grid_forget()

    if selected_rat == "Carrion Rats":
        carrion_rats_photo_label.grid(row=6, columnspan=3)
    elif selected_rat == "Pack Rat":
        pack_rat_photo_label.grid(row=6, columnspan=3)
    else:
        message_txt.insert(0.0, "You are not authorized!")
        restricted_photo_label.grid(row=6, columnspan=3)

magic_rats = Tk()

magic_rats.geometry("310x480")
magic_rats.title("Magic Rats")

welcoming = Label(magic_rats, text="Welcome, Rat Master.", fg="black", font=("arial", 16, "bold"))
question = Label(magic_rats, text="What is thy bidding?", fg="black", font=("arial", 12))
order = Label(magic_rats, text="Summon:", fg="black", font=("arial", 12, "bold"))

rat_entry = StringVar()
rat_entry.set("Carrion Rats") # default value
rat_dropdown = OptionMenu(magic_rats, rat_entry, "Carrion Rats", "Pack Rat")
summon_button = Button(magic_rats, text="Summon!", font=("arial", 12), command=lambda: show_info())

magic_rats.grid_rowconfigure(3, minsize=20)
message_txt = Text(magic_rats, width=16, height=1, wrap=WORD, fg="red", font=("arial", 20, "bold"))

carrion_rats_img = PhotoImage(file="carrion_rats.gif")
carrion_rats_photo_label = Label(magic_rats, image=carrion_rats_img)
pack_rat_img = PhotoImage(file="pack_rat.gif")
pack_rat_photo_label = Label(magic_rats, image=pack_rat_img)

# Layout setup:
welcoming.grid(row=0, columnspan=3)
question.grid(row=1, columnspan=1)
rat_dropdown.grid(row=3, sticky=E)
summon_button.grid(row=4, sticky=E)

message_txt.grid(row=5, columnspan=3, sticky=N, rowspan=1)

magic_rats.mainloop()