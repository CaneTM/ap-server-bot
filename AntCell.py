class AntCell:
    def __init__(self, canvas, x1, y1, c):
        self.color = ''
        self.canvas = canvas
        self.cell = canvas.create_rectangle(x1, y1, x1+c, y1+c, outline='')

    def change_color(self, color):
        self.canvas.itemconfig(self.cell, fill=color)
        self.color = color
