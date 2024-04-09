#SE TIENE QUE USAR UN RELATIVE PATH

#LIBRERÍAS UTILIZADAS:
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

#DIRECTORIOS DE LAS FOTOS:
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Imad Laichi\Desktop\python\app 6\build\assets\frame0")

#FUNCIÓN DE LOS DIRECTORIOS:
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

#CONFIGURACIÓN DE LA VENTANA:
window = Tk()
window.title("Calculador De Procesos Industriales By Imad Industrial Solutions")
window.geometry("1174x700")
window.configure(bg="#FFFFFF")

#FONDO DE LA GUI:
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

#TEXTO DE BIENVENIDA:
canvas.create_text(
    12.0,
    16.0,
    anchor="nw",
    text="Bienvenido al simulador de procesos industriales.\n Aquí podrás simular tu proceso industrial y analizarlo!",
    fill="#24386A",
    font=("Inter Regular", 22 * -1)
)

#ENTRADA DE TEXTO 1:
entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(591.5, 109.0, image=entry_image_1)
entry_1 = Entry(bd=0, bg="#89ABD8", fg="#000716", highlightthickness=0)
entry_1.place(x=564.0, y=86.0, width=55.0, height=44.0)

#ENTRADA DE TEXTO 2:
entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(332.5, 297.5, image=entry_image_2)
entry_2 = Text(bd=0, bg="#89ABD8", fg="#000716", highlightthickness=0)
entry_2.place(x=53.0, y=194.0, width=559.0, height=205.0)
entry_2.config(state="normal")

#ENTRADA DE TEXTO 3:
entry_image_3 = PhotoImage(file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(336.0, 567.0, image=entry_image_3)
entry_3 = Text(bd=0, bg="#89ABD8", fg="#000716", highlightthickness=0)
entry_3.place(x=60.0, y=448.0, width=552.0, height=236.0)
entry_3.config(state="normal")

canvas.create_rectangle(848.0, 53.0, 1135.0, 641.0, fill="#89ABD8", outline="")

#TEXTO 1:
canvas.create_text(
    30.0,
    102.0,
    anchor="nw",
    text="¿Cuántas estaciones quieres que tenga tu industria?",
    fill="#24386A",
    font=("Inter Regular", 20 * -1)
)

#TEXTO 2:
canvas.create_text(
    23.0,
    163.0,
    anchor="nw",
    text="Introduce la producción en unidades/hora (u/h) para cada estación:",
    fill="#24386A",
    font=("Inter Regular", 20 * -1)
)

#TEXTO 3:
canvas.create_text(
    275.0,
    416.0,
    anchor="nw",
    text="RESULTADOS:",
    fill="#24386A",
    font=("Inter Regular", 20 * -1)
)

#TEXTO 4:
canvas.create_text(
    999.0,
    666.0,
    anchor="nw",
    text="Imad Laichi",
    fill="#24386A",
    font=("Imprima Regular", 24 * -1)
)

#FOTOS UTILIZADAS:
image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(994.0, 419.0, image=image_image_2)

image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(991.0, 279.0, image=image_image_3)

image_image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(991.0, 137.0, image=image_image_4)

image_image_5 = PhotoImage(file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(991.0, 557.0, image=image_image_5)

#FUNCIÓN PARA EL BOTÓN 2:
def button2_clicked():
    num_estaciones = int(entry_1.get())
    entry_2.config(state="normal")
    entry_2.delete("1.0", "end")
    for i in range(1, num_estaciones + 1):
        entry_2.insert("end", f"\nIntroduce la producción en unidades/hora (u/h) de la estación {i}: ")
    entry_2.config(state="normal")

#FUNCIÓN PARA EL BOTÓN 1:
def button1_clicked():
    entry_3.config(state="normal")
    entry_3.delete("1.0", "end")

    producciones_estaciones = entry_2.get("1.0", "end").strip().split("\n")

    n_estaciones = len(producciones_estaciones)
    temps_ciclo = []
    lead_time = []

    for i in range(n_estaciones):
        produccion = float(producciones_estaciones[i].split(":")[-1].strip())
        calcular_tiempo_ciclo = 60 / produccion
        temps_ciclo.append(calcular_tiempo_ciclo)
        lead_time = sum(temps_ciclo)

    entry_3.insert("end", "TIEMPOS DE CICLO:\n")
    for i in range(n_estaciones):
        entry_3.insert("end", f"El tiempo de ciclo de la Estación {i+1}: {temps_ciclo[i]:.0f} min/uni\n")

    entry_3.insert("end", f"\nLEAD TIME:\nEl lead time es de: {lead_time:.1f} minutos\n")

    takt_time = max(temps_ciclo)
    entry_3.insert("end", f"\nTAKT TIME:\nEl takt time de la industria es de: {takt_time} minutos\n")

    coll_de_botella = temps_ciclo.index(max(temps_ciclo)) + 1
    entry_3.insert("end", f"\nCOLL DE BOTELLA:\nLa estación que está haciendo cuello de botella es la estación: {coll_de_botella}     \n")
    entry_3.config(state="normal")

    wip = lead_time * 1/takt_time
    entry_3.insert("end",f"\nWORK IN PROGRESS:\nEl work in progress es de : {wip} unidades\n")
    entry_3.config(state="disabled")

#BOTÓN 1:
button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=button1_clicked,
    relief="flat"
)
button_1.place(x=671.0, y=274.0, width=106.0, height=48.0)

#BOTÓN 2:
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
