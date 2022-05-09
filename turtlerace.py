import time
import turtle
from random import randint

turtle.Screen().bgcolor("light blue")
turtle.title("TURTLE RACE")

#creating the turtle objects
james = turtle.Turtle()
james.shape("turtle")
james.color("red")

george = turtle.Turtle()
george.shape("turtle")
george.color("green")

harry = turtle.Turtle()
harry.shape("turtle")
harry.color("blue")

#move the turtles to the starting position
james.up()
george.up()
harry.up()

james.backward(100)
george.goto(-100,100)
harry.goto(-100,-100)

#creating the tracks
james.color("black")
james.goto(-80,125)
james.down()
james.right(90)

#draws 14 tracks
starting_point = -80 #the x-coordinate the tracks will start being drawn from
for i in range(15):
    starting_point = starting_point + 20
    james.write(i+1)
    james.forward(250)
    james.up()
    james.goto(starting_point,125)
    james.down()
james.up()
james.goto(-100,0) 
james.color("red")
james.left(90)

#moving the turtles with random function
james.down()
george.down()
harry.down()

time.sleep(1) #pause the game before starting for 1 second

#the "and" will make it so that the game will end once one of them crosses the finish line (which is at xcor = 200)
while james.xcor() <= 200 and george.xcor() <= 200 and harry.xcor() <= 200: 
    james.forward(randint(1,5)) 
    george.forward(randint(1,5))
    harry.forward(randint(1,5))

jamespost = james.xcor()
georgepost = george.xcor()
harrypost = harry.xcor()

print("James at: ",jamespost)
print("George at: ", georgepost)
print("Harry at: ", harrypost)

if (jamespost < georgepost) and (jamespost < harrypost):
    print("James Wins")
elif(jamespost < georgepost) and (harrypost < jamespost):
    print ("Harry Wins")
elif(georgepost < harrypost):
    print("George Wins")
else:
    print("Harry Wins")


turtle.exitonclick()