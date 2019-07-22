import random, tkinter

def rgb(rgb):
    return "#%02x%02x%02x" % rgb

WIDTH,HEIGHT,MAX_RAD = 1600,1600,200


root = tkinter.Tk()
canvas = tkinter.Canvas(root, width=WIDTH, height=HEIGHT)
class PaintBall:
    def __init__(self):
            self.pos = [random.randrange(WIDTH), random.randrange(HEIGHT)]
            self.rad = random.randrange(MAX_RAD)
            self.color = (random.randrange(256),random.randrange(256),random.randrange(256))
    def draw(self, canvas):
            canvas.create_oval(self.pos[0]-self.rad, self.pos[1]-self.rad, 
                               self.pos[0]+self.rad, self.pos[1]+self.rad,
                               fill=rgb(self.color))


def update():
    PaintBall().draw(canvas)
    root.after(random.randrange(10), update)
update()

canvas.pack()
root.mainloop()

