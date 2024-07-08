from pyfirmata import Arduino
import time
import tkinter as tk

window = tk.Tk()
window.config(background='black')
window.state('zoomed')
window.title('Play Arduino')


board = Arduino('COM23')

pin_13 = board.get_pin('d:13:o')

def on():
    pin_13.write(1)
def off():
    pin_13.write(0)

button1 = tk.Button(window, text = 'ON', font = ('Arial', 40), command = lambda:on())
button1.place(x  = 50, y = 50)
window.mainloop()