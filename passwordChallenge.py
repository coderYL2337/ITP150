#Lab #8
#ITP 150 12/1/2022
#Author Name: Yan Lu
#File Name: passwordChallenge.py

import tkinter
from tkinter import simpledialog


def main():
    print("Programmed By : Yan Lu")
    #prompt user to enter a password according to the rules
    passwd=simpledialog.askstring("ITP150",'''Please enter a password according to the following rules:
                                                     Minimum of 8 characters
                                                     Maximum of 15 characters
                                                     Cannot contain @
                                                     Cannot contain a space
                                                     MUST end with a numeric
                                                     MUST contain one of these characters     !    &    %
                                                     Password MUST begin with an alpha
                                                 ''')

    #set inital value of valid to False, so we can enter the while loop 
    valid=False

    #while loop check if password entered by user follows all the rules
    #if any rule is broken, ask user to reenter password, check rule compliance till a password meeting all rules is entered 
    while(valid==False):
        valid=validatePasswd(passwd)
        if valid==False:
           print("Invalid Password !!")
           print()
           passwd=simpledialog.askstring("ITP150",'''Please enter a password according to the following rules:
                                                     Minimum of 8 characters
                                                     Maximum of 15 characters
                                                     Cannot contain @
                                                     Cannot contain a space
                                                     MUST end with a numeric
                                                     MUST contain one of these characters     !    &    %
                                                     Password MUST begin with an alpha
                                                 ''')
        
    print("Password is valid.")

        

  
# Function to validate the password
def validatePasswd(passwd):
      
    SpecialSym =['!', '&', '%']
    val = True
    last=passwd[len(passwd)-1]
    first=passwd.strip()[0]

    #check if password has minimum of 8 characters, if not, print out alert, assign False to val 
    if len(passwd) < 8:
        print('Password must has minimum of 8 characters')
        val = False
        
    #check if password  has maximum of 15 characters, if not, print out alert, assign False to val 
    if len(passwd) > 15:
        print('Password must has maximum of 15 characters')
        val = False

    #check if password ends with a numeric,if not, print out alert, assign False to val 
    if (last.isnumeric()==False):
       print('Password must end with a numeric')
       val=False
       
    #check if password contains @, if yes, print out alert, assign False to val  
    if passwd.count("@")>0:
       print('Password cannot contain @')
       val=False

    #check if password contains space, if yes, print out alert, assign False to val  
    if passwd.count(" ")>0:
       print('Password cannot contain a space')
       val=False

    #check if password contains at least one of the symbols ! & %   if not, print out alert, assign False to val 
    if not any(char in SpecialSym for char in passwd):
        print('Password should have at least one of the symbols ! & %')
        val = False

    #check if passowrd begins with alpha, if not,print out alert, assign False to val 
    if (first.isalpha()==False):
        print('Password must begin with an alpha')
        val = False

    # return the True or False value of val to main().If all rules met, val stays True. If any rule breaks val is False. 
    return val

#call main() function
main()
