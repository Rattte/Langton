from operator import index
import turtle
from webbrowser import get
import time
  
def langton():
    
    
    size = 1000
    #bigger number = faster
    updates = 10000
    
    #less ants = faster
    Antcount = 1
    
    
  
    # Initializing the Window
    window = turtle.Screen()
    window.bgcolor('white')
    window.screensize(size,size)
    antsize = 0.1
  
    # Contains the coordinate and colour
    maps = {}
    LR = [("black","R"),("white","L")]
    LLRR = [("blue","L"), ("pink","R"), ("black","R"),("white","L")]
    LLRRRLRLRLLR = [("blue","L"), ("pink","R"), ("green","R"), ("azure","R"), ("cyan","L"), ("beige","R"), ("olive","L"), ("gold","R"), ("goldenrod","L"), ("yellow","L"), ("black","R"),("white","L")]
    LRL = [("black","R"),("blue","L"),("white","L")]
    LLRL = [("black","R"),("green","L"),("blue","L"),("white","L")]
    LLRLR = [("goldenrod","L"), ("black","R"),("green","L"),("blue","R"),("white","L")]
    RRLLLRLLLRRR = [("blue","R"), ("pink","L"), ("green","L"), ("azure","L"), ("cyan","R"), ("beige","L"), ("olive","L"), ("gold","L"), ("goldenrod","R"), ("yellow","R"), ("black","R"),("white","R")]
    turtle.delay(0)
    ants = []
    for i in range(Antcount):
        ants.append(turtle.Turtle())
        ants[i].shape('square')    
      
        # size of the ant
        ants[i].shapesize(antsize)
        # speed of the ant
        ants[i].speed(0)     
        ants[i].ht()
    step = antsize*20   
    #disable turtle update
    turtle.tracer(0,0)    
    # gives the coordinate of the ant                
    antcolour = RRLLLRLLLRRR           
    count = 0

    totalcount = 0
    while len(ants) > 0:
        
        #time.sleep(1)
        for ant in ants:
            totalcount +=1
            
            pos = coordinate(ant)    
            count+=1          
            # distance the ant will move
                                              
            if pos not in maps or maps[pos] == "white":
                ant.fillcolor(antcolour[0][0])
                ant.stamp()
                invert(maps, ant, antcolour[0][0])
                ant.left(90)
                ant.forward(step)
                
                pos = coordinate(ant)   
                
            else:
                #find index of colour
                for i in antcolour:
                    
                    if i[0] == maps[pos]:
                        ind = antcolour.index(i)+1 
                        if antcolour.index(i)>=len(antcolour):
                            ind = 0
                        ant.fillcolor(antcolour[ind][0])
                        ant.stamp()
                        invert(maps,ant,antcolour[ind][0])
                        if i[1]=="R":
                            ant.right(90)
                        else:
                            ant.left(90)
                        ant.forward(step)
                        pos=coordinate(ant)
                        break
            if count >= updates:
                turtle.update()
                count=0
            if abs(ant.xcor()) >= size/2 or abs(ant.ycor()) >= size/2:
                ants.pop(ants.index(ant))
                print("ant finished after ",totalcount," steps")
            if totalcount %1000 == 0:
                print(totalcount)
    while True:
        turtle.update()
        window.exitonclick()
    
        
def invert(graph, ant, color):
    graph[coordinate(ant)] = color
    
  
def coordinate(ant):
    return (round(ant.xcor()), round(ant.ycor()))



def llrr():
    pass
    
  
langton()