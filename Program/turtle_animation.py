import turtle


def show_animation() :

    a = turtle.Turtle()

    a.speed(0.23)
    turtle.bgcolor("black")
    a.width = 10

    for i in range(20) :
        a.color("cyan")
        a.circle(i)
        a.left(7)

    turtle.done()

show_animation()