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
  
    #Start of the story. Mainly text with a few loops and input statements.

    print("")
    print("--------")
    print("Prologue") 
    print("--------")
    print("")
    print("TEN YEARS BEFORE")
    print("")
    time.sleep (5)
    character_name = input("What is your name: ")
    time.sleep (2)
    print("After a long and hard day at school you come home to watch your favourite gameshow.")
    time.sleep(3)
    print('You tell yourself "I wanna make it up there one day!"')
    time.sleep(3)  
    print("The host reveals that in order to get a HUGE prize you need to answer ALL 30 questions correctly. He also reveals that if you mess up even one question there will be a HUGE punishment. ") 
    time.sleep (5)
    print('You see this super nerdy kid step on stage to answer questions and you think to yourself "BRUH That is literally me!"')
    time.sleep (3)
    print("Then a guy who practically looks homeless walks on stage")
    time.sleep (3)
    print('You spit your water out and start laughing the hardest you have ever laughed before. You scream out, "HOW IN THE WORLD DID HE GET INTO THE GAMESHOW!?!"')
    time.sleep (3)
    print("The host starts spitting out questions.")
    time.sleep (3)
    print("Question after question the homeless looking guy answers everything correctly while the super nerdy kid couldn't seem to even get a single question right")
    time.sleep (5)
    print('You are like "This is crazy HOW IS THIS HAPPENING?!?"')
    time.sleep (1.5)
    print("After the 10th question it became clear that the nerd was absolutely no match for the homeless guy")
    time.sleep (3)
    print('The 30th question seemed absolutely impossible, "State the first 100 digits of pi." Seemed like an impossible task or so you thought. The homeless guy made it look like he was counting to 100 while the nerd looked like he was going to cry. ')
    time.sleep (5)
    print('As soon as they finished the final question, they quickly pulled a curtain over the stage and ended the show, You are like, "Damn thats kinda SUS, I wanna know what happens behind there." ')
    print("")
    print("END OF PROLOGUE")

    print("10 YEARS PASS")
    print("You are now a junior in high school. You went from a nerd to a huge idiot. Your parents also kicked you out of the house for watching too much anime and not studying enough.")
    time.sleep (3)
    print("You are a couch hopper and all your friends despise you.")
    time.sleep (3)
    print("When all seems lost you get an email inviting you to a huge gameshow.")
    time.sleep (3)
    print("You get a feeling of nostalgia and realize that this is the same gameshow as the one you saw on TV 10 years ago.")
    time.sleep (3)
    gameshow_answer = input("Do you want to accept or not: ")

while gameshow_answer.lower().strip() != "yes":
    print("You are out of food and have nowhere to sleep you must say yes.") 
    gameshow_answer = input("Do you want to accept or not: ")

if gameshow_answer.lower().strip() == "yes":
    print("You accept the invitation and prepare to get your life back together. ")
    time.sleep (3)
    print("You visit the gameshow website and it says that the topic of the gameshow is all TECH.")
    time.sleep (3)
    print("You start studying tech topics because you remember that you have to answer every question correctly. You remember the super SUS curtain that they pulled over the stage and it motivates you to study hard so you can win and see what happens behind the curtain.")
    time.sleep (5)
    print("As you study you reminisce about your life as a kid when you used to be a nerd. You realize that you really messed up your life and that you could have been very successful if you did not start watching anime every day.")
    time.sleep (5)
    print("You study hard every day in preparation for the gameshow which is in a week.")
    time.sleep (3)
    print("")
    print("ONE WEEK PASSES")
    print("")
    print("You take the bus to the gameshow arena dressed in your regular clothes.")
    time.sleep (3)
    print("You walk in looking homeless, you feel the eyes staring at you and the giggles that they are holding back.")
    time.sleep (3)
    print('You tell yourself "I am going to prove all these people wrong and win this gameshow!"')
    time.sleep (3)
    print("As you step on stage you see your opponent, a slim, tall nerd. You feel a bit nervous but you also remind yourself that you should not judge a book by its cover because of what you saw on TV 10 years ago")
    time.sleep (5)
    print('You are insanely focussed and you hear the host start speaking. "Please welcome ' + character_name + ' and Sean who will be your contestants today!"')
    time.sleep (5)
    print(character_name + " and Sean please tell the audience a little bit about yourself")
    time.sleep (5)
    information_about_player = input("Tell the audience a little bit about yourself: ")
    print(information_about_player)
    time.sleep (5)
    print("And you Sean?")
    time.sleep (5)
    print("Hi, my name is Sean and some of my hobbies are studying, watching videos on how to do math and coding. I am very confident that I will win this gameshow!")
    print('After we talked to the audience for a bit the host told us the rules of the gameshow. "You must answer every question correctly to get a prize or you will get a huge punishment."')
    print("Then he immediately started spitting out questions")

    
#elif statement to quit game if user types no
elif play.lower().strip() == "no":
    print("")
    time.sleep(1.5)
    print("Come Back Soon!")



        




