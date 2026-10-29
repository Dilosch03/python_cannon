"""Cannon, hitting targets with projectiles.

Exercises

1. Keep score by counting target hits.
2. Vary the effect of gravity.
3. Apply gravity to the targets.
4. Change the speed of the ball.
"""

from random import randrange
from turtle import *

from freegames import vector

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []
ball_speed_base = 250
balloon_colors = ["yellow","green","blue","purple"]
ballon_speeds = [0.1,0.5,1,2]


def tap(x, y):
    """Respond to screen tap."""
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + ball_speed_base) / 25
        speed.y = (y + ball_speed_base) / 25


def inside(xy):
    """Return True if xy within screen."""
    return -200 < xy.x < 200 and -200 < xy.y < 200


def draw():
    """Draw ball and targets."""
    clear()

    for target_loc,target_speed in targets:
        goto(target_loc.x, target_loc.y)
        dot(20, balloon_colors[target_speed])

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()


def move():
    """Move ball and targets."""
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        target_speed = randrange(4)
        targets.append((target,target_speed))

    for target_loc,targ_speed in targets:
        target_loc.x -= targ_speed

    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target[0] - ball) > 13:
            targets.append(target)

    draw()

    for target in targets:
        if not inside(target[0]):
            target[0].x = 200
            target[0].y = randrange(-150, 150)

    ontimer(move, 50)


setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
