#program to create Madlib game for kids
#i -name1, location, liquid, object1
#p -get inputs from the user and concatenate them into a line of the story
#o -a funny story
#declare variables
name1=""
location=""
liquid=""
object1=""
print("Welcome to Madlib 150")

#get input from users keyboard 
name1=input("What is the name of your best friend?")
location=input("What is your favorite place to play?")
liquid=input("What is your favorite drink?")
object1=input("What is something important to you?")

#output a story          
print("Jack and",name1)
print("Went up the",location)
print("To fetch a pail of",liquid)
print("Jack fell down")
print("And broke his",object1)
print("And", name1,"came tumbling after")