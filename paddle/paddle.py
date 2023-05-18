import turtle
import time

SCREEN_WIDTH=760
SCREEN_HEIGHT=600
def init_screen():
    w = turtle.Screen()
    w.title("Paddle Game")
    w.bgcolor("black")
    w.setup(width=SCREEN_WIDTH,height=SCREEN_HEIGHT)
    w.tracer(0)
    return w

def make_ball():
    b=turtle.Turtle()
    b.speed(0)
    b.color("white smoke")
    b.shape("circle")
    b.penup()
    b.goto(3,4)
    return b

def make_paddle():
    p=turtle.Turtle()
    p.speed(0)
    p.color("light pink")
    p.shape("square")
    p.shapesize(1, 5)
    p.penup()
    p.goto(0,-250)
    return p

def init_key_listener(s):
    s.listen()
    s.onkey(paddle_right,"Right")
    s.onkey(paddle_left,"Left")

def paddle_right():
    x,y=paddle.position()
    if x<300:
        paddle.setpos(x+80 , y)

def paddle_left():
    x,y=paddle.position()        
    if x>-300:
        paddle.setpos(x-80 , y)

def init_score_writer():
    pen=turtle.Turtle()
    pen.speed(0)
    pen.shape("square")
    pen.color("honeydew")
    pen.penup()
    pen.hideturtle()
    return pen

def make_block1(b):
    block1=[]
    x=-340
    for i in range(7):
        b=turtle.Turtle()
        b.speed(0)
        b.shape("square")
        b.color("lime")
        b.shapesize(1, 5)
        b.penup()
        b.goto(x,280)
        block1.append(b)
        x=x+110
    return block1

def make_block2(c):
    block2=[]
    x=-340        
    for j in range(7):
        c=turtle.Turtle()
        c.speed(0)
        c.shape("square")
        c.color("cyan")
        c.shapesize(1, 5)
        c.penup()
        c.goto(x,255)
        block2.append(c)
        x=x+110
    return block2

def make_block3(d):
    block3=[]
    x=-340        
    for j in range(7):
        d=turtle.Turtle()
        d.speed(0)
        d.shape("square")
        d.color("yellow")
        d.shapesize(1, 5)
        d.penup()
        d.goto(x,230)
        block3.append(d)
        x=x+110
    return block3

def make_block4(d):
    block4=[]
    x=-340        
    for j in range(7):
        d=turtle.Turtle()
        d.speed(0)
        d.shape("square")
        d.color("red")
        d.shapesize(1, 5)
        d.penup()
        d.goto(x,205)
        block4.append(d)
        x=x+110
    return block4

def make_blocks(block1,block2,block3,block4):
    blocks=[]
    blocks.append(block1)
    blocks.append(block2)
    blocks.append(block3)
    blocks.append(block4)
    return blocks

def ball_move(a , make_blocks):
    x,y=ball.position()
    a.speed(0)
    a.penup()
    a.goto(ball.xcor()+ball.dx,ball.ycor()+ball.dy)
    for b in make_blocks:
        if b.xcor()-55<=ball.xcor()<=b.xcor()+55 and b.ycor()<=ball.ycor()<=b.ycor()+25 :
            b.color("black")
            a.dy=a.dy*-1
            b.penup()
            b.goto(1000,1000)
            #make_blocks.remove(b) 
            return True

def paddle_check():
    if paddle.ycor()<=ball.ycor()<=paddle.ycor()+15:
        if ball.xcor()>=paddle.xcor()-55 and ball.xcor()<=paddle.xcor()+55:
            ball.dy=ball.dy*-1

def border_check():
    if ball.xcor()>=350 or ball.xcor()<=-350:
        ball.dx=ball.dx*-1
    if ball.ycor()>290 :
        ball.dy=ball.dy*-1 

def border_check_reset():
    if ball.ycor()<=-300 :
        ball.goto(0,0)
        return True

def update_score(score,high_score):
    score_writer.undo()
    score_writer.hideturtle()
    score_writer.goto(-220,-250)
    s = "Score: {} High score: {} ".format(score , high_score)
    score_writer.write(s , align="center" ,font=("Courier",16, "normal")) 

scrn=init_screen()  
ball=make_ball()  
paddle=make_paddle()
ball.dx=5
ball.dy=5
score_writer=init_score_writer()
init_key_listener(scrn)
make_blocks=make_block1(ball)+make_block2(ball)+make_block3(ball)+make_block4(ball)
score=0
high_score=0

while True :

    if ball_move(ball,make_blocks)==True:
        score=score+10
        if score>high_score:
            high_score=score
    paddle_check()
    border_check()
    if border_check_reset()==True:
        score=0

    update_score(score,high_score)
    scrn.update()
    time.sleep(.00015)