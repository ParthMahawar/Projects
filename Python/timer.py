import time
from tkinter import *

for i in range(100):
	print(i/100)
	time.sleep(.00000001)

root = Tk()
canvas = Canvas(root, width = 50, height = 10)
canvas.pack()
canvas.create_line(0, 0, 200, 20)
mainloop()