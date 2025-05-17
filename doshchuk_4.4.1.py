import turtle
import time
import math
from datetime import datetime

class Watch:
    def __init__(self):
        self.running = True

    def update(self):
        pass

class Цифра:
    def __init__(self, x, y, текст):
        self.x = x
        self.y = y
        self.текст = текст
        self.малюй()

    def малюй(self):
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(self.x, self.y)
        t.write(self.текст, align="center", font=("Arial", 14, "normal"))

class Циферблат:
    def __init__(self, радіус=200):
        self.радіус = радіус
        self.малюй_циферблат()

    def малюй_циферблат(self):
        turtle.mode("logo")
        for i in range(1, 13):
            кут = math.radians(i * 30)
            x = self.радіус * math.sin(кут)
            y = self.радіус * math.cos(кут)
            Цифра(x, y, str(i))

class Стрілка:
    def __init__(self, довжина, товщина, колір):
        self.довжина = довжина
        self.курсор = turtle.Turtle()
        self.курсор.hideturtle()
        self.курсор.speed(0)
        self.курсор.pensize(товщина)
        self.курсор.color(колір)

    def малюй(self, кут):
        self.курсор.clear()
        self.курсор.penup()
        self.курсор.goto(0, 0)
        self.курсор.setheading(90)
        self.курсор.right(кут)
        self.курсор.pendown()
        self.курсор.forward(self.довжина)

class AnalogWatch(Watch):
    def __init__(self):
        super().__init__()
        Циферблат()
        self.годин = Стрілка(100, 6, "black")
        self.хвилин = Стрілка(140, 3, "blue")
        self.секунд = Стрілка(160, 1, "red")
        self.update()

    def update(self):
        now = datetime.now()
        s = now.second
        m = now.minute
        h = now.hour % 12 + m / 60
        self.секунд.малюй(s * 6)
        self.хвилин.малюй(m * 6)
        self.годин.малюй(h * 30)
        turtle.ontimer(self.update, 1000)

class DigitalWatch(Watch):
    def __init__(self, формат_24=True):
        super().__init__()
        self.формат_24 = формат_24
        self.text = turtle.Turtle()
        self.text.hideturtle()
        self.text.penup()
        self.text.goto(0, -250)
        self.text.color("green")
        self.update()

    def update(self):
        now = datetime.now()
        h = now.hour
        m = now.minute
        s = now.second
        if not self.формат_24:
            suffix = "AM" if h < 12 else "PM"
            h = h % 12 or 12
            time_str = f"{h:02}:{m:02}:{s:02} {suffix}"
        else:
            time_str = f"{h:02}:{m:02}:{s:02}"
        self.text.clear()
        self.text.write(time_str, align="center", font=("Courier", 20, "bold"))
        turtle.ontimer(self.update, 1000)

if __name__ == "__main__":
    turtle.Screen().bgcolor("white")
    AnalogWatch()
    DigitalWatch(формат_24=False)
    turtle.mainloop()
