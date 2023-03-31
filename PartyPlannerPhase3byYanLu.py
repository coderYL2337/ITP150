#Project-phase3 11/30 2022 ITP150
#Reqirement P3-7: comment code
#File name: PartyPlanner.py
#This program will help calculate how many food and drinks to order and plan party activities based on party type and weather.
#Programmed by: Yan Lu
#i -numAdult, numChildren, partyType,temp,weather
#p -calculate number of pizzas to order using fromula numPizza = math.ceil((numAdult * 3 + numChildren * 2) / 8);
#p -calculate number of sodas to order using fromula numSoda=math.ceil((numAdult*5+numChildren*3)/12);
#p --calculate number of beers to order using fromula numBeer=math.ceil(numAdult*3/24);
#p--calculate estimated cost of pizzas, sodas, beers and the total cost
#p-generate party activities based on party type and weather.
#p -generate random number between 1 and 5, each number corresponds to a song album.
#o -print out numPizza,numSoda,numBeer needed;print out estimated cost for pizza, soda, beer and total estimated cost; print out partyActivity option;print out song album choice

import tkinter
from tkinter import messagebox
from tkinter import simpledialog
import math
import random
import datetime



#def main module
def main():
    #Declare Numeric Variables
    numAdult = 0
    numChildren = 0
    again=True
    count=1
    index=0
    #P3-1 Create, load and use a pair of parallel Lists and load with meaningful data.
    #fbList is a list of food and beverage items.
    fbList=["x"]*3
    #parallel lsit. priceList is a list of corresponding prices for food and beverage items in fbList.
    priceList=[0]*3

    f1=open("file1.txt","r")
    f2=open("file2.txt","r")

    
    foodDrinkItem=f1.readline()
    itemPrice=f2.readline()

    
    while(foodDrinkItem):
       fbList[index]=foodDrinkItem.strip()
       priceList[index]=int(itemPrice)
       index+=1
       foodDrinkItem=f1.readline()
       itemPrice=f2.readline()
    print(fbList)
    print(priceList)
   


#user the readline() method to read the data from the txt file
#use a loop to process the file
#read the file until it is empty
#initial read of the line



#loop the rest of the records in the txt file
#while loop will stop when the file is empty




    print("Programmed By : Yan Lu") 
    
    
    #Welcome the user using a dialog box
    messagebox.showinfo("Welcome to the Party Planner", "Let's calculate the food and beverages to order and plan party activities.")
    
    print(f'''          party {count}      ''')
    
    #call getPartyDate(), get Party Date
    getPartyDate()
    
    #call getNumAdult(),assign returned value to numAdult
    numAdult=getNumAdult()

    #call getNumChildren(), assign returned value to numChildren
    numChildren=getNumChildren()
  
    
    #call getFoodBeverage() function, get food and beverages needed based on numAdult and numChildren
    getFoodBeverage(numAdult,numChildren,fbList,priceList)
    
    #call getPartyActivities() funtion, get party activities
    getPartyActivities()
    
    #call getPartyAlbum() function,get name of music album to play at party
    getPartyAlbum()

    #output blank line, to seperate planned parties
    print('''
          ''')
    #call anotherParty(),ask if user wants to plan another party.Count the number of parties planned.
    count=anotherParty(again,count,fbList,priceList)

    #wrap up message
    print("Thank you for using our party planner!")
    print(f"You planned {count} party this time.")

    f1.close()
    f2.close()


#function getNumAdult.Prompt user to enter number of adults at the party, return and assign value to numAdult in main()
def getNumAdult():
    numAdult1=0
    numAdult1=simpledialog.askinteger("Party Planner","Please enter the number of adults at the party: ")
    numAdult1=validNumAdult(numAdult1)
    return numAdult1

#P3-5.  Make sure that ALL of the user inputs are either validated or default to an acceptable value.  Your program should not blow up, if I enter the wrong data.
def validNumAdult(numAdultN):
    while numAdultN<0:
        numAultN=simpledialog.askinteger("Party Planner","Error! Enter valid number of adults (0,1,2...)")
    return numAdultN

#function getNumAdult.Prompt user to enter number of children at the party, return and assign value to numChildren in main()
def getNumChildren():
    numChildren1=0
    numChildren1=simpledialog.askinteger("Party Planner","Please enter the number of children at the party: ")
    numChildren1=validNumChildren(numChildren1)
    return numChildren1

def validNumChildren(numChildrenN):
    while numChildrenN<0:
        numChildrenN=simpledialog.askinteger("Party Planner","Error! Enter valid number of children (0,1,2...)")
    
    return numChildrenN

  
    
#function getPartydate(). Prompt user to enter year, month and day of month for the planned party.Validate user input. Output date and day of week.    
def getPartyDate():
    dateYear=0
    dateMonth=0
    dateDay=0
    #Prompt user to enter year of the party
    dateYear=simpledialog.askinteger("Party Planner","Please enter year of the party(2022/2023)")
    #call validYear(), validate user's input of year 
    dateYear=validYear(dateYear)
    
    #Prompt user to enter month of the party
    dateMonth=simpledialog.askinteger("Party Planner","Please enter month of the party （1-12）")
    #call validMonth(), validate user's input of month 
    dateMonth=validMonth(dateMonth)

    #Prompt user to enter day of month of the party
    dateDay=simpledialog.askinteger("Party Planner","Please enter day of month of the party （1-31）")
    #call validDay(), validate user's input of day of month 
    dateDay=validDay(dateMonth,dateDay)

    #Requirement P2-8.  Get date in the format of xxxx-xx-xx by using datetime.date()
    #get party date and assign to x.
    x = datetime.date(dateYear, dateMonth, dateDay)

    #call validDate(),validate if date for planned party is not past.
    x=validDate(x)

    #Requirement P2-8.  Get day of week based on date.
    #get weekday based on user input,full version
    y=x.strftime("%A")
    
    #output party date and weekday
    print(f"Party Date: {x}  {y}")

#function validYear(), party planning can only be for the year of 2022 or 2023.
def validYear(dateYear1):
    #requirement P2-2 Error-validation loop
    while dateYear1!=2022 and dateYear1!=2023:
          dateYear1=simpledialog.askinteger("Party Planner","Error!Enter year of the party(2022/2023)")
    return dateYear1
    
#function validMonth(), month for planned party can only be 1-12   
def validMonth(dateMonth1):
    #requirement P2-2 Error-validation loop
    while dateMonth1>12 or dateMonth1<1:
          dateMonth1=simpledialog.askinteger("Party Planner","Error!Enter month of the party(1-12)")
    return dateMonth1
    
#function validDay(), day of month for planned party must be 1-31. Feburary only has 28 days.
def validDay(dateMonth1,dateDay1):
    #requirement P2-2 Error-validation loop
    while dateDay1>31 or dateDay1<1:
          dateDay1=simpledialog.askinteger("Party Planner","Error!Enter day of month of the party(1-31)")
    dateDay1=check30dayMonth(dateMonth1,dateDay1)
    dateDay1=check28dayMonth(dateMonth1,dateDay1)
    return dateDay1

#function check30dayMonth(). validate user input of day of month. For April,June,September, and November, there are only 30 days.         
def check30dayMonth(dateMonth1,dateDay1):
         #requirement P2-2 Error-validation loop
          while (dateMonth1==4 or dateMonth1==6 or dateMonth1==9 or dateMonth1==11)and(dateDay1>30 or dateDay1<1):
                 dateDay1=simpledialog.askinteger("Party Planner","Error! Reenter day of month (1-30)")
          return dateDay1
            
#function check28dayMonth(). validate user input of day of month.For Feburary, there are only 28 days.  
def check28dayMonth(dateMonth1,dateDay1):
         #requirement P2-2 Error-validation loop
          while (dateMonth1==2)and (dateDay1>28 or dateDay1<1):
                 dateDay1=simpledialog.askinteger("Party Planner","Error! Reenter day of month (1-28)")
          return dateDay1
          
    
#function validDate().validate if user input of date is not past. return value of validated date to x in main()
def validDate(x1):
    
    nowDate=datetime.date.today()
    #requirement P2-2 Error-validation loop
    while x1<nowDate:
        messagebox.showinfo("Party Planner","Error! You entered a past date. Please enter a future or current date.")
        dateYear=simpledialog.askinteger("Party Planner","Please enter year of the party(2022/2023)")
        #validation of user's input of year 
        dateYear=validYear(dateYear)
        
        #Prompt user to enter month of the party
        dateMonth=simpledialog.askinteger("Party Planner","Please enter month of the party （1-12）")
        #validation of user's input of month 
        dateMonth=validMonth(dateMonth)

        #Prompt user to enter day of month of the party
        dateDay=simpledialog.askinteger("Party Planner","Please enter day of month of the party （1-31）")
        #validation of user's input of day of month 
        dateDay=validDay(dateMonth,dateDay)
     
        x1 = datetime.date(dateYear, dateMonth, dateDay)
    return x1
          
    
    
    
#Requirement P2-5.  Include the main() function and at least one more function . Receive two arguments and return a value. 
#calculate how many Pizzas to order depending oon number of adults and children.Receive argument of numAdult1 and numChildren from main module, and return value of numSoda1 back to main module, 
def getNumPizza(numAdult1,numChildren1):
    numPizza1=0
    numPizza1=math.ceil((numAdult1 * 3 + numChildren1 * 2) / 8)
    return numPizza1
    
#Requirement P2-5.  Include the main() function and at least one more function . Receive two arguments and return a value. 
#calculate how many cases of 12pk soda to order depending oon number of adults and children.Receive argument of numAdult1 and numChildren from main module, and return value of numSoda1 back to main module, 
def getNumSoda(numAdult1,numChildren1):
    numSoda1=0
    #Each adult can have 5 sodas. Each child can have 3 sodas.
    numSoda1=math.ceil((numAdult1*5+numChildren1*3)/12)
    return numSoda1


#function getNumBeer(), calculate how many cases of 24 pk beer to order depending on number of adults.  Receive argument of numAdult1 from main module, and return value of numBeer1 back to main module, 
def getNumBeer(numAdult1):
    #Each adult can have 3 beers.
    numBeer1=math.ceil(numAdult1*3/24)
    return numBeer1

def getPizzaCost(numPizza2,fbList2,priceList2):
    idx=fbList2.index("pizza")
    pricePizza=priceList2[idx]
    costPizza2=numPizza2*pricePizza
    return costPizza2
    
def getSodaCost(numSoda2,fbList2,priceList2):
    idx=fbList2.index("soda")
    priceSoda=priceList2[idx]
    costSoda2=numSoda2*priceSoda
    return costSoda2

def getBeerCost(numBeer2,fbList2,priceList2):
    idx=fbList2.index("beer")
    priceBeer=priceList2[idx]
    costBeer2=numBeer2*priceBeer
    return costBeer2



#function getFoodBeverage(), calculate Pizza, soda and beer needed,estmated cost for pizza,soda and beer, total estimated cost and print out results
def getFoodBeverage(numAdult1,numChildren1,fbList1,priceList1):
    numPizza=0
    numSoda=0
    numBeer=0
    costPizza=0
    costSoda=0
    costBeer=0
    costTotal=0
    numPizza=getNumPizza(numAdult1,numChildren1)
    numSoda=getNumSoda(numAdult1,numChildren1)
    numBeer=getNumBeer(numAdult1)
    costPizza=getPizzaCost(numPizza,fbList1,priceList1)
    costSoda=getSodaCost(numSoda,fbList1,priceList1)
    costBeer=getBeerCost(numBeer,fbList1,priceList1)
    costTotal=costPizza+costSoda+costBeer
    
    
    #print out number of adult and children at party. 
    print(f"Number of Adults: {numAdult1}  Number of Children: {numChildren1}")
    #print out number of pizza to be ordered
    #RequirementP2-6.  Display a pizza emoji that is related to the topic of my application.
    print(f"\U0001f355 Pizzas to be ordered: {numPizza} Estimated cost: ${costPizza}")
    #print out number of soda to be ordered
    #RequirementP2-6.  Display soda emoji that is related to the topic of my application.
    print(f"\U0001f964 12pack sodas to be ordered: {numSoda} case(s) Estimated cost: ${costSoda} ")
    #print out number of beer to be ordered
    #RequirementP2-6.  Display beer emoji that is related to the topic of my application.
    print(f"\U0001f37a 24pack beers to be ordered: {numBeer} case(s) Estimated cost: ${costBeer} ")
    print(f"Estimated total cost for this party : ${costTotal}")
    
#function validaPartyType(),validate user input of preferred party type. 
def validPartyType(partyType1):
    #requirement P2-2 Error-validation loop
    while partyType1!="home" and partyType1!="pool":
          partyType1=simpledialog.askstring("Party Planner","Error! Please enter your preferred party type: home or pool")
          partyType1=partyType1.lower()
    return partyType1

#function validaWeather(),validate user input of weather.
def validWeather(weather1):
    #requirement P2-2 Error-validation loop
    while weather1!="RAINY" and weather1!= "RAIN" and weather1!= "HAILS" and weather1!= "SNOW" and weather1!= "SNOWY" and weather1!="CLOUDY" and weather1!="SUNNY" and weather1!="WINDY" : 
          weather1=simpledialog.askstring("Party Planner","Error!Enter weather: Sunny/Cloudy/Rainy/Snowy/Windy/Hails")
          weather1=weather1.upper()
    return weather1
    
#function getPartyActities(), get party activities based on user's preference and weather.    
def getPartyActivities():
    temp=0
    isBadWeather=True
    partyType=""
    weather=""
    badweatherHome = "We can watch a movie, play chess, or play charades."
    goodweatherHome = "We can watch a movie, play chess, play charades, or play soccer outside."
    outsidePool = "We can go swimming or chat with other non-swimmers."
    partyActivity=""
    #message dialog box
    messagebox.showinfo("Party Planner", "Now let's plan party activities based on party type and weather.")
    #Inputs dialog box;Prompt the user to enter your inputs
    partyType=simpledialog.askstring("Party Planner","Please enter your preferred party type: home or pool")
    partyType=partyType.lower()
    partyType=validPartyType(partyType)
    temp=simpledialog.askinteger("Party Planner","Please enter the temperature in Fahrenheit on the day of party: ")
    weather=simpledialog.askstring("Party Planner","What is the weather on the day of party?Sunny/Cloudy/Rainy/Snowy/Windy/Hails")
    weather=weather.upper()
    weather=validWeather(weather)

    # Requirement P2-1 At least one compound condition (OR)
    if weather=="RAINY" or weather== "RAIN" or weather== "HAILS" or weather== "SNOW" or weather== "SNOWY"  : 
       isBadWeather=True;
    else:
       isBadWeather=False;
    #Outputs
    print("Preferred party type: " + partyType)
    print("Temperature: " +str(temp)+ " F   "+"Weather: "+weather)
     
  
    if isBadWeather:
       if partyType.upper()=="POOL":
       #Outputs
          print("We cannot have an outdoor pool party due to the weather. It must be at home instead." )
          print(badweatherHome);
       else:
       #Outputs
           print(badweatherHome);

    elif partyType.upper()=="POOL":
         # Requirement P2-1 At least one compound condition (AND)
         if (temp>=75 and isBadWeather==False):
            print("The weather is good. We can have a outside pool party.")
            print(outsidePool);
         elif isBadWeather:
             print("We cannot have an outdoor pool party due to the weather. It must be at home instead." )
             print(badweatherHome);   
         else:
            print("The weather is not hot enough. We cannot have a outside pool party.")
            print(goodweatherHome);
            
    else:
         if ((temp>=50 and temp<=80) and isBadWeather==False):
            print("The weather is nice.")
            print(goodweatherHome);
         elif(temp<50 or temp>80):
            print(badweatherHome);



#funtion getPartyAlbum(), choose which music album to play by random
def getPartyAlbum():  
    albumChoice=0
    albumPlay=""  
    #generate a random number between 1 and 6, assign value to albumChoice
    albumChoice=random.randrange(1,6)
    #find matching albumChoice title based on albumChoice number
    if albumChoice==1:
       albumPlay="The Beetles";
    elif albumChoice==2:
       albumPlay="Carpenters";
    elif albumChoice==3:
       albumPlay="The Fame";
    elif albumChoice==4:
       albumPlay="Britney";
    else :
       albumPlay="MADONNA";

    #Outputs print out title of album to be played
    #RequirementP2-6.  Display music emoji that is related to the topic of my application.
    print(f"\U0001f3b5  Album to be played at the party: {albumPlay} ")

#funtion anotherParty(),ask user if they want to plan another party, loop party planning process if user answers yes. Count the number of parties planned.return count value to main()
def anotherParty(again1,count1,fbList1,priceList1):
    again1=messagebox.askyesno("Party Planner","Do you want to plan another party?")
    #Requirement P2-3.At least one other loop (in addition to the error-validation loop).
    while(again1):
        #Requirement P2-4. At least one abbreviated incrementor (count+=1)
        count1+=1
        
        print(f'''          party {count1}      ''')
        #get Party Date
        getPartyDate()
      
        #call getNumAdult(),assign returned value to numAdult
        numAdult=getNumAdult()

        #call getNumChildren(), assign returned value to numChildren
        numChildren=getNumChildren()
        
        #call getFoodBeverage() function
        getFoodBeverage(numAdult,numChildren,fbList1,priceList1)
        #call getPartyActivity() funtion
        getPartyActivities()
        #call getPartyAlbum() function
        getPartyAlbum()
        print('''
        ''')
        again1=messagebox.askyesno("Party Planner","Do you want to plan another party?")
    return count1
    

#call main module
main()

    
   
