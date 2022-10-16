import enum
from operator import index
import random
import turtle
from webbrowser import get
import time
import io
from PIL import Image
  
def langton():
    R,r = "R", "R"
    L,l = "L","L"
    
    #size of board
    size = 1000
    
    #bigger number = faster
    updates = 40000
    
    #less ants = faster
    Antcount = 1
    
    #best size is 0.1
    antsize = 0.1
    
    # 0 = fastest
    speed = 0
    
    #different rules
    LR = ("L","R") #normal
    LLRR = [L,L,R,R] #square
    LLRRRLRLRLLR = [l,l,r,r,r,l,r,l,r,l,l,r] #big highway
    LRL = [l,r,l] #highway instantly
    LLRL = [l,l,r,l] #highway instantly
    LLRLR = [l,l,r,l,r] #random
    RRLLLRLLLRRR = [r,r,l,l,l,r,l,l,l,r,r,r]
    RRLRRLLLLRRR = [r,r,l,r,r,l,l,l,l,l,r,r,r] #Square
    LLLLR = [l,l,l,l,r] #random?
    LRLRLRLL = [l,r,l,r,l,r,l,l]  #random?
    LLRRRLRLRLLL = [l,l,r,r,r,l,r,l,r,l,l,l] 
    RRLLRRRL = [r,r,l,l,r,r,r,l] 
    LRLRLLLRLR = [l,r,l,r,l,l,l,r,l,r]
    LLLLLRR = [l,l,l,l,l,r,r]
    lrlrlrlrllr = [l,r,l,r,l,r,l,r,l,l,r]
    LLLLLLLLLR = [l,l,l,l,l,l,l,l,l,l,l,r]
    LLLRRRLRLRRRLRLLRLRLR = [l,l,l,r,r,r,l,r,l,r,r,r,l,l,r,l,r,l,r,l,r]
    
    #choose which rule to use
    rule = LLLRRRLRLRRRLRLLRLRLR   
    
    
    
    # Initializing the Window
    window = turtle.Screen()
    window.bgcolor('white')
    window.screensize(size,size)

    
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
    
    
    #set the rules for the ant
              
    antcolour = []       
    turtle.colormode(255)   
    
    length = len(rule)
    #add colors to list
    for i in range(length):
        if i == 0:
            antcolour.append([rule[i],(255,255,255)])
        elif i == length-1:
            antcolour.append([rule[i],(0,0,0)])
        else:
            antcolour.append([rule[i],(random.randint(0,255),random.randint(0,255),random.randint(0,255))])
        
        
    # Contains the coordinate and colour
    maps = {}
    count = 0

    totalcount = 0
    while len(ants) > 0:
        time.sleep(speed)
        
        #time.sleep(1)
        for ant in ants:
            totalcount +=1
            
            pos = coordinate(ant)    
            count+=1          
            # distance the ant will move
                                              
            if pos not in maps or maps[pos] == (0,0,0):
                ant.fillcolor(antcolour[0][1])
                ant.stamp()
                invert(maps, ant, antcolour[0][1])
                if antcolour[-1][0] == "L":
                    ant.left(90)
                else:
                    ant.right(90)
                ant.forward(step)
                
                pos = coordinate(ant)   
                
            else:
                #find index of colour
                for i in antcolour:
                    
                    if i[1] == maps[pos]:
                        ind = antcolour.index(i)+1 
                        if antcolour.index(i)>=len(antcolour):
                            ind = 0
                        ant.fillcolor(antcolour[ind][1])
                        ant.stamp()
                        invert(maps,ant,antcolour[ind][1])
                        if i[0]=="R":
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