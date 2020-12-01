def matchstick_game():
    print('''\n========================>>>>\n\n"Hey!! Welcome to the matchstick_game".\n\nHere are the rules ======> \n   
    1.There are 21 matchsticks.
    2.The computer asks the player to pick 1, 2, 3, 4 matchsticks.
    3.After the person picks, the computer does its picking.
    4.Whoever is forced to pick up the last matchstick loses the game.\n==============================>>>>''')
    a ='yes'
    while a=='yes':
      matchstick = 21
      while matchstick <= 21:
         print("Total matchstick = ", matchstick)
         user_choice = int(input("Choose a number from 1 to 4\n"))
         if user_choice > 4 or user_choice < 1:
            print("error")
            break
         computer_choice = 5 - user_choice
         print("Computer's choice is =", computer_choice)
         matchstick = matchstick - user_choice - computer_choice
         if matchstick == 1:
            print("Total matchstick = ", matchstick)
            print("You lost!!")
            break
      a = input("Do you want to play matchstick_game again? yes/no \n")
      if a != 'yes':
         print('Hey!! Thanks for Playing matchstick_game ')





def number_guess_game():
   print('\n"Hey!! Welcome to number_guess_game"\n\n=========================>>>>>')
   import random
   a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
   number = random.choice(a)
   guess = int(input('Please Enter Number Between (1 - 20)\n'))
   nguess = 1
   while number != guess :
      if guess >20 or guess < 0:
         print("Error")
         break
      if guess < number :
         print("Pls! Enter Higher Number")
      if guess > number :
         print("Pls! Enter Lower Number")
      nguess += 1
      guess = int(input())
   if number == guess :
      print("You Won the Game in ",nguess)
      print("Guesses\nThnx For Playing number_guess_game!!")










def umang_game():
   c = 'yes'
   while c == 'yes':
      print('\n"Welcome!! To Fun_Fact_game"\n\n====================>>>>>"')
      a = input("enter your birth month(eg. June) \n").lower()
      b = int(input("Enter your birth date(eg. 26)\n"))
      d = int(input("Enter your birth year(eg. 2002)\n"))

      data = {"january": "I kicked", "february": "I kissed", "march": "I slapped", "april": "I fucked", "may": "I missed",
            "june": "I loved", "july": "I punched", "august": "I licked", "september": "I cuddled with",
            "october": "I ate", "november": "I made out with", "december": "I wrestled"}

      data2 = {1: "my lover", 2: "my partner", 3: "a toothbrush", 4: "Aristotle", 5: "a glass of vodka", 6: "a porn star",
             7: "my bff", 8: "a condom", 9: "my bae", 10: "a dog", 11: "my bike", 12: "a baby", 13: "the watchman",
             14: "an easter egg", 15: "a stripper", 16: "a hooker", 17: "a policeman", 18: "my bestie", 19: "a volleyball",
             20: "a bitch", 21: "my best friend", 22: "a bowl of cereal", 23: "a golf ball", 24: "a donkey",
             25: "a bowl of french fries", 26: "a mob", 27: "my professor", 28: "the toilet", 29: "a landmine",
             30: "a bull", 31: "a burger"}

      data3 = {1995: "in the park.", 1996: "at coffee shop.", 1997: "in hotel.", 1998: "in bathroom.", 1999: "in dreams.",
             2000: "in bedroom.", 2001: "in college.", 2002: "in bathtub.", 2003: "on the terrace.", 2004: "at gym."}
      print("Your remark is : \n\n", data[a], data2[b], data3[d])
      c = input("Do you want to play again? Fun_Fact_game (yes/no) \n")
      if c != 'yes':
         print("Thnx for Playing Fun_Fact_game")







def tejaswi_game():
   print("\nWelcome!! to Treasure Hunting Game\n=======================>>>>>")
   answer=input("would you like to go on an adventurous journey ?('yes' or 'no')\n")
   if answer =="yes":
      # name = input("what's your good name\n")
      # print('name')
      print('''One day you found a old treasure  map and you decide to found the treasure..\nafter following the path on map you drop the map and lost it ''')
      answer=input("And reached a crossroad, would you like to take ('left' or 'right') ?\n").lower()
      if answer=="left":
         answer=input("you encounter a monster , would you like to attack with stone or run('attack' or 'run') ?\n")
         if answer=="attack":
            print("this was not the good idea, monster killed you. you lost! ...better luck next time")
         else:
            print("good choice, you made it away safely") 
            answer=input("you see an old bridge and river  . which would you like to take?  ('car' or 'plane')\n")
            if answer=="car":
               print("Unfortunately the bridge was to weak and break because of your weight GAME OVER..")
            else:
               print("you found the treasure..congratulation")   
      elif answer=="right":
         print("you walk away to the right and fall on a patch of ice .you injured your leg and cannot continue,GAME OVER!")
      else:
         print("Invalid choice, you lost")
   else:
      print("That's too bad!we will play next time ")





def abhay_game():
   import random
   Cchoice=["Rock","Paper","Scissor"]              # list for computer 
   while True:
      print("Rock Paper scissor Game:\n")
      youwin,computerwin=0,0
      for i in range(1,6):                    # 5 Round game
         print("Round",i,"Start:")
         print("Please select any one option:")
         print("1.Rock(Pls Enter 1)","2.Paper(Pls Enter 2)","3.Scissor(Pls Enter 3)",sep="\n")  # choice any option but in number 1,2,3
         Yourchoice=int(input())
         if Yourchoice==1:
            print("You select Rock")
            Yourchoice="Rock"
         elif Yourchoice==2:
            print("You select paper")
            Yourchoice="Paper"
         elif Yourchoice==3:
            print("You select scissor")
            Yourchoice="Scissor"
         else:
            print("Invalid Choice")
            break
         Computerchoice=random.choice(Cchoice)  #random select by computer choice
         print("Computer select:",Computerchoice)
# comparing result and give the point.
         if Yourchoice==Computerchoice:    
            print("This Round is Draw:")
         elif (Yourchoice=="Paper" and Computerchoice=="Rock") or (Yourchoice=="Rock" and Computerchoice=="Scissor") or(Yourchoice=="Scissor" and Computerchoice=="Paper"):
            youwin+=1
            print("You win this Round")
         else:
            computerwin+=1
            print("Computer win this Round")
# if your point more than computer then you win and vice versa
      if youwin>computerwin:
         print("You Win the game:")
         print("Score is:","Your score:",youwin,"Computer score:",computerwin,sep=" ")
      elif computerwin>youwin:
         print("You Lose the game. Computer win the game:")
         print("Score is:","Your score:",youwin,"Computer score:",computerwin,sep=" ")
      else:
         print("Match Draw")
         print("Score is:","Your score:",youwin,",Computer score:",computerwin,sep=" ")
      user_choice=input("Want to Play again?(Yes/Exit)\n")
      if user_choice=='yes' or user_choice=='Yes' or user_choice=='YES':
         continue             
      else:
         break


d='yes'
while d=='yes':

   print('''\n"Hey!! Welcome To the Cosec Gaming World!"\n\n========================>>>>\nWhich Game Do You Want To Play\n
   1. Matchstick_Game (Pls! Enter 1)\n   2. Number_Guess_Game (Pls! Enter 2)\n   3. Fun_Fact_Game (Pls! Enter 3)
   4. Treasure_Hunting_Game (Pls! Enter 4)\n   5. ROCK_PAPER_SCISSOR_Game (Pls! Enter 5)''')
   game = int(input())
   if game == 1:
      matchstick_game()
   if game == 2:
     number_guess_game()
   if game == 3:
      umang_game()
   if game == 4:
      tejaswi_game()
   if game == 5:
      abhay_game()
   d = input("Do You Want To Play Another Game? (yes/no)\n")
print("Thnx For Playing Cosec Games!!")