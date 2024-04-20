import random
import turtle

screen = turtle.Screen()
screen.bgcolor('Light Blue')
screen.title('Catch The Turtle')
FONT = ('Arial', 20, 'normal')
grid_size = 10
score = 0
game_over = False


#score turtle

score_turtle = turtle.Turtle()

#countdown turtle

countdown_turtle = turtle.Turtle()


#turtlelist
turtle_list = []

def setup_score_turtle():
    score_turtle.hideturtle()
    score_turtle.color('red')
    score_turtle.penup()


    score_turtle.setpos(0,290)
    score_turtle.write(arg= 'Score:0', move=False, align='Center', font=FONT)

def make_turtle(x,y):

    def handle_click(x,y):
        print(x,y)
        global score
        score+= 1
        score_turtle.clear()
        score_turtle.write(arg=f'Score:{score}', move=False, align='Center', font=FONT)

    t = turtle.Turtle()


    t.onclick(handle_click)
    t.penup()
    t.shape('turtle')
    t.color('purple')
    t.goto(x*grid_size,y*grid_size)
    turtle_list.append(t)

x_coordinates = [-20,-10,0,10,20]
y_coordinates = [20,10,15,-10]

def setup_turtles():
    for x in x_coordinates:
        for y in y_coordinates:
            make_turtle(x,y)

def hide_turtles():
    for t in turtle_list:
        t.hideturtle()


#recursive function
def show_turtles_randomly():
    if not game_over:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        screen.ontimer(show_turtles_randomly, 500)




def countdown(time):
    global game_over
    countdown_turtle.hideturtle()
    countdown_turtle.color('red')
    countdown_turtle.penup()

    countdown_turtle.setpos(0,240)
    countdown_turtle.clear()

    if time > 0:
        countdown_turtle.clear()
        countdown_turtle.write(arg=f'time:{score}', move=False, align='Center', font=FONT)
        screen.ontimer(countdown(time - 1), 500)

    else:
        game_over = True
        countdown_turtle.clear()
        hide_turtles()
        countdown_turtle.write(arg='Game Over', move=False, align='Center', font=FONT)
























def start_game_up():
    turtle.tracer(0)
    setup_score_turtle()
    setup_turtles()
    hide_turtles()
    show_turtles_randomly()
    countdown(10)
    turtle.tracer(1)



start_game_up()
turtle.mainloop()
