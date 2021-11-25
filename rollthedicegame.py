# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 17:45:29 202
Travel around the entire game board of 20 spaces within 5 die rolls.
*roll the die for player (generate a random number between 1-6 and advance that user that number of spaces on the game board.)
*after each roll, tell the user which game space they are on and how many more spaces they have to go to win
* repeat this 4 aditional times for 5 rolls in total.
*if the user gets to 20 before 5 rolls, end the game - they've won


"""

import random
import time


lastspace=20
max_rolls=5
current_space=0
i=0
ready = "yes"


print("Welcome to the Dice game, To win you have a max of 5 rolls and need to roll a 20. All the best")

ready = input("Press enter to roll...")
      
while i<=max_rolls: 
    print("rolling dice...")
    time.sleep(1)
    die = random.randint(1,6)
    current_space = ((current_space)+(die))
    print("Roll number " + str((i)+1)+ " and you have rolled a " + str(die))
    i+=1
    
    if current_space == lastspace:
        print("Your on " + str(current_space) + " CONGRATS! you Win!")
        break
    if current_space > lastspace:
        print("Unfortunately You're on space " + str(current_space) + ". Sorry you Loose")
        break
    if (i == max_rolls) and (current_space <lastspace):
        print("Sorry you did not get to " + str(lastspace) + " You loose")
        break
    else:
        spaces_to_win = lastspace - current_space
        print("You're on space " + str(current_space) + " and need " + str(spaces_to_win) + " spaces to Win")
        ready = input("Press enter to roll...")
            
        
   






"""

        int lastspace = 20;
        int maxRolls = 5;
        int currentSpace = 0;

        Random random = new Random();

        System.out.println("Welcome to the Dice game, To win you have a max of 5 rolls and need to roll a 20. All the best");

       for(int i=1; i<=maxRolls; i++ ){
           int die = random.nextInt(6) +1;
           currentSpace = currentSpace + die;

           System.out.println(String.format("Roll #%d: You've rolled a %d. ", i, die));

           if (currentSpace == lastspace){
               System.out.println("Your on " + currentSpace + " CONGRATS! you win!");
               break;
           }

           else if(currentSpace > lastspace){
               System.out.println("Unfortunately You're on space " + currentSpace + ". Sorry you loose");
               break;
           }
           else if (i==maxRolls && currentSpace <lastspace){
               System.out.println("Sorry you did not get to "+ lastspace + " You loose");
               break;

           }
           else{
               int spacesToGo = lastspace - currentSpace;
               System.out.println("You are now on space "+ currentSpace + " and have "+ spacesToGo + " more to go");
           }
        System.out.println();
        
        """