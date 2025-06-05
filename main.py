import tkinter as tk
import threading
import time
import pyautogui

ex = False

def anti_afk():
    while ex:
        pyautogui.keyDown('w')
        time.sleep(0.5)
        pyautogui.keyUp('w')
        time.sleep(0.8)
        pyautogui.keyDown('s')
        time.sleep(0.5)
        pyautogui.keyUp('s')
        time.sleep(5)

def iniciar():
    global ex
    if not ex:
        ex = True
        threading.Thread(target=anti_afk, daemon=True).start()
        estado.set("Estado: Activo")

def detener():
    global ex
    ex = False
    estado.set("Estado: Detenido")

ventana = tk.Tk()
ventana.title("Anti-AFK")
ventana.geometry("200x100")

estado = tk.StringVar(value="Estado: Detenido")

tk.Label(ventana, textvariable=estado).pack(pady=5)
tk.Button(ventana, text="Iniciar", command=iniciar).pack(pady=5)
tk.Button(ventana, text="Detener", command=detener).pack(pady=5)

ventana.mainloop()