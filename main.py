import time
'''
--------------------------
Name: Deadly Gameshow 
Purpose: Demonstrate course material in an interesting and entertaining way 

Author: John Zhang

Created: date 03/24/2021
--------------------------
'''

#asks user if they would like to play or quit
play = input("Would you like to play? Yes or No: ") 

#while loop to keep repeating until the user types in a viable option
#also using .lower() and .strip() to remove white spaces and convert word to lowercase so the user doesn't break the code easily. 
while play.lower().strip() != "yes" and play.lower().strip() != "no": 
    #Incorporating time.sleep() from time function to slow down the game and make it easier to read
    time.sleep(1.5)
    print ("Type a viable option!")
    time.sleep(1.5)
    play = input("Would you like to play? Yes or No: ")

#if statement to continue game if user types yes
if play.lower().strip() == "yes":
    print("")
    time.sleep(1.5)
    print("---------------")
    print("Deadly Gameshow")
    print("---------------")
    print("")
    time.sleep(2)
    print("You'll be able to play shortly.")
    time.sleep(4)
  
    #Start of the story. This the main starting point.
    print("")
    print("--------")
    print("Prologue") 
    print("--------")

    print("TEN YEARS BEFORE")
    time.sleep (5)
    print("After a long and hard day at school you come home to watch your favourite gameshow.")
    time.sleep(3)
    print('You think to yourself "Damn, I wanna be up there one day!"')
    time.sleep(3)  
    print("The caster reveals that in order to get a HUGE prize you need to answer ALL 30 questions correctly. He also reveals that if you mess up even one question there will be a HUGE punishment. ") 
    time.sleep (5)
    print('You see this super nerdy kid step on stage to answer questions and you think to yourself "BRUH That is literally me!"')
    time.sleep (3)
    print("Then a guy who practically looks homeless walks on stage")
    time.sleep (3)
    print('You spit your water out and start laughing "HOW IN THE WORLD DID HE GET INTO THE GAMESHOW!?!"')
    time.sleep (3)
    print("You hear the caster start asking questions and as a super nerdy 7 year old you understood absolutely everything")
    time.sleep (3)
    print("Question after question the pratically homeless guy answers everything correctly while the super nerdy kid couldn't seem to even get a single question right")
    time.sleep (5)
    print("HOW IS THIS HAPPENING?!?")
    time.sleep (1.5)
    print("After the 10th question it became clear to you that the nerd was absolutely no match for the homeless guy")
    time.sleep (3)
    print('The 30th question "State the first 100 digits of pi." Seemed like an imposibble task or so you thought. The homeless guy made it look like he was counting to 100 while the nerd looked like he was going to cry. ')
    time.sleep (5)
    print('They quickly pulled a curtain over the stage and ended the show, you think to yourself, "Damn thats kinda sus, I wanna know what happens behind there one day." ')



  

  


    print("")

#elif statement to quit game if user types no
elif play.lower().strip() == "no":
  print("")
  time.sleep(1.5)
  print("Come Back Soon!")
  


        




