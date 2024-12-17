import turtle
from counter_board import Counterboard
from button import Button

screen = turtle.Screen()
screen.setup(width=2000, height=1125)
screen.title("Job Applications")
image = "week6/Job_Application/job_application.gif"
screen.addshape(image)
turtle.shape(image)


def on_click(x, y):
    print(f"You clicked x:{x}, y:{y}")


# Draw a circle at -9, 152
# When user clicks it, update the counter

counterboard = Counterboard()

job_app_button = Button(position=(-7, 29), color ="blue", callback=counterboard.job_app_point)
success_button = Button(position=(-360, -270), color ="green", callback=counterboard.success_point)
reject_button = Button(position=(360, -270), color="red", callback=counterboard.reject_point)

screen.onclick(on_click)

screen.mainloop()