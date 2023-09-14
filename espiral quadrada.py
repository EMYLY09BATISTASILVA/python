import turtle

pen = turtle.Turtle()
wn.bgcolor("white")
skk = turtle.Turtle()
skk.color("blue")
#cor = ['red','green','yellow']
skk.pensize(1)

def sqrfunc(size):
    for i in range(4):
        #skk.color(cor[i % len(cor)])
        skk.fd(size)
        skk.right(90)
        size = size +10
        #size += 10
        pen.forward(i * 20) 
        

    

sqrfunc(6)
sqrfunc(36)
sqrfunc(66)
sqrfunc(96)
sqrfunc(126)
sqrfunc(156)
sqrfunc(186)

