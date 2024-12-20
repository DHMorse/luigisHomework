from tkinter import Tk, Canvas
from random import randrange, choice
from typing import List

# Constants for canvas dimensions
CANVAS_WIDTH: int = 600
CANVAS_HEIGHT: int = 400

class Ball:
    def __init__(self, x: int, y: int, radius: int, color: str, xvel: float, yvel: float, canvas: Canvas) -> None:
        self.x: float = x
        self.y: float = y
        self.radius: int = radius
        self.color: str = color
        self.xvel: float = xvel
        self.yvel: float = yvel
        self.canvas: Canvas = canvas
        self.circle = self.canvas.create_arc(
            x - radius, y - radius, x + radius, y + radius,
            extent=359, width=1, style="pieslice", outline=color, fill=color
        )

    def move(self) -> None:
        self.yvel += 0.2
        self.x += self.xvel
        self.y += self.yvel
        self.xvel *= 0.998
        self.yvel *= 0.998
        self._check_for_wall_hit()
        self.canvas.coords(
            self.circle, self.x - self.radius, self.y - self.radius,
            self.x + self.radius, self.y + self.radius
        )
        self.canvas.after(10, self.move)

    def _check_for_wall_hit(self) -> None:
        if self.x < self.radius:
            self.xvel = -self.xvel
            self.x += 2 * (self.radius - self.x)
        if self.x > CANVAS_WIDTH - self.radius:
            self.xvel = -self.xvel
            self.x -= 2 * (self.x + self.radius - CANVAS_WIDTH)
        if self.y < self.radius:
            self.yvel = -self.yvel
            self.y += 2 * (self.radius - self.y)
        if self.y > CANVAS_HEIGHT - self.radius:
            self.yvel = -self.yvel
            self.y -= 2 * (self.y + self.radius - CANVAS_HEIGHT)

def generate_random_color() -> str:
    hexdigits: str = "ABCDEF0123456789"
    return "#" + "".join(choice(hexdigits) for _ in range(6))

def create_balls(canvas: Canvas, num_balls: int) -> List[Ball]:
    balls: List[Ball] = []
    for _ in range(num_balls):
        radius: int = randrange(3, 24)
        x: int = randrange(100, 500)
        y: int = randrange(50, 350)
        xvel: int = randrange(-8, 8)
        yvel: int = randrange(-8, 8)
        color: str = generate_random_color()
        balls.append(Ball(x, y, radius, color, xvel, yvel, canvas))
    return balls

def main() -> None:
    root: Tk = Tk()
    canvas: Canvas = Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="black")
    canvas.pack()

    balls: List[Ball] = create_balls(canvas, 10)
    for ball in balls:
        ball.move()

    root.mainloop()

if __name__ == "__main__":
    main()
