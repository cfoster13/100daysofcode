from turtle import Turtle

class Button(Turtle):
    def __init__(self, position, color, callback):
        super().__init__()
        self.shape("circle")
        self.shapesize(2, 2)
        self.color(color)
        self.penup()
        self.goto(position)
        self.callback = callback
        self.onclick(self.on_click)

    def on_click(self, x, y):
        if self.callback:
            self.callback()

    
        