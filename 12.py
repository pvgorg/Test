import turtle

t = turtle.Turtle()

# Drawing the girl
t.fillcolor('pink')
t.begin_fill()
t.circle(50)
t.end_fill()

t.penup()
t.goto(20, 60)
t.pendown()
t.fillcolor('black')
t.begin_fill()
t.circle(10)
t.end_fill()

t.penup()
t.goto(-20, 60)
t.pendown()
t.fillcolor('black')
t.begin_fill()
t.circle(10)
t.end_fill()

t.penup()
t.goto(0, 40)
t.pendown()
t.fillcolor('red')
t.begin_fill()
t.circle(7)
t.end_fill()

# Drawing the boy
t.penup()
t.goto(100, 0)
t.pendown()
t.fillcolor('blue')
t.begin_fill()
t.circle(50)
t.end_fill()

t.penup()
t.goto(80, 60)
t.pendown()
t.fillcolor('black')
t.begin_fill()
t.circle(10)
t.end_fill()

t.penup()
t.goto(120, 60)
t.pendown()
t.fillcolor('black')
t.begin_fill()
t.circle(10)
t.end_fill()

t.hideturtle()

turtle.done()
