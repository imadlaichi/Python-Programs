#USED LIBRARIES:
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

#DIRECTORY OF THE PHOTOS:
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Imad Laichi\Desktop\python\app 6\build\assets\frame0")

#FUNCTION OF THE DIRECTORIES:
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

#WINDOW CONFIGURATION:
window = Tk()
window.title("Industrial Process Calculator By Imad Industrial Solutions")
window.geometry("1174x700")
window.configure(bg="#FFFFFF")

#GUI BACKGROUND:
canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=700,
    width=1174,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)
image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(587.0, 350.0, image=image_image_1)

#WELCOME TEXT:
canvas.create_text(
    12.0,
    16.0,
    anchor="nw",
    text="Welcome to the industrial process simulator. Here you can simulate and analyze your industrial process!",
    fill="#24386A",
    font=("Inter Regular", 22 * -1)
)
#TEXT INPUT 1:
entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(591.5, 109.0, image=entry_image_1)
entry_1 = Entry(bd=0, bg="#89ABD8", fg="#000716", highlightthickness=0)
entry_1.place(x=564.0, y=86.0, width=55.0, height=44.0)
#TEXT INPUT 2:
entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(332.5, 297.5, image=entry_image_2)
entry_2 = Text(bd=0, bg="#89ABD8", fg="#000716", highlightthickness=0)
entry_2.place(x=53.0, y=194.0, width=559.0, height=205.0)
entry_2.config(state="normal")
#TEXT INPUT 3:
entry_image_3 = PhotoImage(file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(336.0, 567.0, image=entry_image_3)
entry_3 = Text(bd=0, bg="#89ABD8", fg="#000716", highlightthickness=0)
entry_3.place(x=60.0, y=448.0, width=552.0, height=236.0)
entry_3.config(state="normal")

canvas.create_rectangle(848.0, 53.0, 1135.0, 641.0, fill="#89ABD8", outline="")
#TEXT 1:
canvas.create_text(
    30.0,
    102.0,
    anchor="nw",
    text="How many stations do you want your industry to have?",
    fill="#24386A",
    font=("Inter Regular", 20 * -1)
)
#TEXT 2:
canvas.create_text(
    23.0,
    163.0,
    anchor="nw",
    text="Enter the production in units/hour (u/h) for each station:",
    fill="#24386A",
    font=("Inter Regular", 20 * -1)
)
#TEXT 3:
canvas.create_text(
    275.0,
    416.0,
    anchor="nw",
    text="RESULTS:",
    fill="#24386A",
    font=("Inter Regular", 20 * -1)
)
#TEXT 4:
canvas.create_text(
    999.0,
    666.0,
    anchor="nw",
    text="Imad Laichi",
    fill="#24386A",
    font=("Imprima Regular", 24 * -1)
)
#PHOTOS USED:
image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(994.0, 419.0, image=image_image_2)

image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(991.0, 279.0, image=image_image_3)

image_image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(991.0, 137.0, image=image_image_4)

image_image_5 = PhotoImage(file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(991.0, 557.0, image=image_image_5)

#FUNCTION FOR BUTTON 2:
def button2_clicked():
    num_stations = int(entry_1.get())
    entry_2.config(state="normal")
    entry_2.delete("1.0", "end")
    for i in range(1, num_stations + 1):
        entry_2.insert("end", f"\nEnter the production in units/hour (u/h) of station {i}: ")
    entry_2.config(state="normal")

#FUNCTION FOR BUTTON 1:
def button1_clicked():
    entry_3.config(state="normal")
    entry_3.delete("1.0", "end")

    station_productions = entry_2.get("1.0", "end").strip().split("\n")

    n_stations = len(station_productions)
    cycle_times = []
    lead_time = []

    for i in range(n_stations):
        production = float(station_productions[i].split(":")[-1].strip())
        calculate_cycle_time = 60 / production
        cycle_times.append(calculate_cycle_time)
        lead_time = sum(cycle_times)

    entry_3.insert("end", "CYCLE TIMES:\n")
    for i in range(n_stations):
        entry_3.insert("end", f"Cycle time of Station {i+1}: {cycle_times[i]:.0f} min/unit\n")

    entry_3.insert("end", f"\nLEAD TIME:\nThe lead time is: {lead_time:.1f} minutes\n")

    takt_time = max(cycle_times)
    entry_3.insert("end", f"\nTAKT TIME:\nThe takt time of the industry is: {takt_time} minutes\n")

    bottleneck = cycle_times.index(max(cycle_times)) + 1
    entry_3.insert("end", f"\nBOTTLENECK:\nThe station causing bottleneck is station: {bottleneck}     \n")
    entry_3.config(state="normal")

    wip = lead_time * 1/takt_time
    entry_3.insert("end",f"\nWORK IN PROGRESS:\nThe work in progress is: {wip} units\n")
    entry_3.config(state="disabled")

#BUTTON 1:
button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=button1_clicked,
    relief="flat"
)
button_1.place(x=671.0, y=274.0, width=106.0, height=48.0)

#BUTTON 2:
button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=button2_clicked,
    relief="flat"
)
button_2.place(x=661.0, y=85.0, width=105.0, height=48.0)

window.mainloop()
