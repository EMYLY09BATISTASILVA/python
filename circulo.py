import turtle as tt

#fazendo os circulos

tt.bgcolor('black')
tt.speed(100)

for ciclos in range(6):   
    for color in ('red', 'magenta', 'blue',
                  'cyan', 'green',
                    'yellow'):
            tt.color(color)
            tt.circle(100)
            tt.left(10)
         
