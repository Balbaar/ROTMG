import threading
import PySimpleGUI as pg
from scripts import *

pg.theme("DarkTeal4")

layout = [
    [pg.Text("Auto Scripts")],
    [pg.Checkbox("Auto Pot")],
    [pg.Checkbox("Chest Steal")],

    [pg.Button("Apply", )]
]


#Functions
def auto_potion():
    global toggle_autopot
    while toggle_autopot:
        auto_pot()


def chest_stealer():
    global toggle_cheststeal
    while toggle_cheststeal:
        chest_steal()


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

        print(toggle_autopot)
        print(toggle_cheststeal)
        print(threading.active_count())


window.close()
exit()
