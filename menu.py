import threading
import PySimpleGUI as pg
from scripts import *
import keyboard

pg.theme("DarkTeal4")

layout = [
    [pg.Text("Auto Scripts")],
    [pg.Checkbox("Auto Pot")],
    [pg.Checkbox("Chest Steal")],

    [pg.Button("Apply", )]
]


#Functions
def auto_potion():
    while toggle_autopot:
        auto_pot()

    return


def chest_stealer():
    while toggle_cheststeal:
        if keyboard.is_pressed("c"):
            chest_steal()
        else:
            pass
    return


window = pg.Window("ROTMG Scripts", layout, size=(300, 400))

while True:
    event, values = window.read()
    if event == pg.WINDOW_CLOSED:
        break
    if event == "Apply":
        if values[0]:
            toggle_autopot = True
            autopot_thread = threading.Thread(target=auto_potion)
            autopot_thread.start()
        else:
            toggle_autopot = False

        if values[1]:
            toggle_cheststeal = True
            cheststeal_thread = threading.Thread(target=chest_stealer)
            cheststeal_thread.start()
        else:
            toggle_cheststeal = False

        print(threading.active_count())


window.close()
exit()
