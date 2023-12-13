import sys, time, os

def typewriter(message, duration):
  for char in message:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(duration)

def hello_from_monster_ascii():
  typewriter("""
⢀⡴⠑⡄⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠸⡇⠀⠿⡀⠀⠀⠀⣀⡴⢿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠑⢄⣠⠾⠁⣀⣄⡈⠙⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⢀⡀⠁⠀⠀⠈⠙⠛⠂⠈⣿⣿⣿⣿⣿⠿⡿⢿⣆⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⢀⡾⣁⣀⠀⠴⠂⠙⣗⡀⠀⢻⣿⣿⠭⢤⣴⣦⣤⣹⠀⠀⠀⢀⢴⣶⣆ 
⠀⠀⢀⣾⣿⣿⣿⣷⣮⣽⣾⣿⣥⣴⣿⣿⡿⢂⠔⢚⡿⢿⣿⣦⣴⣾⠁⠸⣼⡿ 
⠀⢀⡞⠁⠙⠻⠿⠟⠉⠀⠛⢹⣿⣿⣿⣿⣿⣌⢤⣼⣿⣾⣿⡟⠉⠀⠀⠀⠀⠀ 
⠀⣾⣷⣶⠇⠀⠀⣤⣄⣀⡀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ 
⠀⠉⠈⠉⠀⠀⢦⡈⢻⣿⣿⣿⣶⣶⣶⣶⣤⣽⡹⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠉⠲⣽⡻⢿⣿⣿⣿⣿⣿⣿⣷⣜⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣷⣶⣮⣭⣽⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⣀⣀⣈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠿⠿⠿⠿⠛⠉
    """, 0.01)


def leg_it():
  typewriter("you scarper.", 0.02)
  # exit()


def going_alone_ascii():
  # Function
  # Player went alone ASCII
  print("""
\                           /
 \                         /
  \                       /
   ]                     [    ,'|
   ]                     [   /  |
   ]___               ___[ ,'   |
   ]  ]\             /[  [ |:   |
   ]  ] \           / [  [ |:   |
   ]  ]  ]         [  [  [ |:   |
   ]  ]  ]__     __[  [  [ |:   |
   ]  ]  ] ]\ _ /[ [  [  [ |:   |
   ]  ]  ] ] (#) [ [  [  [ :===='
   ]  ]  ]_].nHn.[_[  [  [
   ]  ]  ]  HHHHH. [  [  [
   ]  ] /   `HH("N  \ [  [
   ]__]/     HHH  "  \[__[
   ]         NNN         [
   ]         N/"         [
   ]         N H         [
  /          N            \
 /           q,            \
/                           \


    """)


# Function
# Snake ASCII
def snake_ascii():
  print("""
    Y
  .-^-.
 /     \      .- ~ ~ -.
()     ()    /   _ _   `.                     _ _ _
 \_   _/    /  /     \   \                . ~  _ _  ~ .
   | |     /  /       \   \             .' .~       ~-. `.
   | |    /  /         )   )           /  /             `.`.
   \ \_ _/  /         /   /           /  /                `'
    \_ _ _.'         /   /           (  (
                    /   /             \  \
                   /   /               \  \
                  /   /                 )  )
                 (   (                 /  /
                  `.  `.             .'  /
                    `.   ~ - - - - ~   .'
                       ~ . _ _ _ _ . ~
    """)
  typewriter(f'You were bitten by a snake {first_name} and suffer a horrible painful death.', 0.02)

def game_over_ascii(first_name):
  
  print("""
        ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
    ███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀
    ██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼
    ██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀
    ██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼
    ███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄
    ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
    ███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼
    ██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼
    ██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼
    ██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼
    ███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄
    ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼████▄┼┼┼▄▄▄▄▄▄▄┼┼┼▄████┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼▀▀█▄█████████▄█▀▀┼┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼┼┼█████████████┼┼┼┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼┼┼██▀▀▀███▀▀▀██┼┼┼┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼┼┼██┼┼┼███┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼┼┼█████▀▄▀█████┼┼┼┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼┼┼┼███████████┼┼┼┼┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼▄▄▄██┼┼█▀█▀█┼┼██▄▄▄┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼▀▀██┼┼┼┼┼┼┼┼┼┼┼██▀▀┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
        """)
  start_again()
def start_game():
  global first_name
  typewriter(f'\nWelcome, {first_name}:\nYou are walking along a forest path and you come across a friendly looking monster \n', 0.05)
  hello_from_monster_ascii()
  typewriter("""The monster smiles and says 'Hello can you help me?'\n""", 0.03)
  typewriter('Enter option yes or no\n>', 0.02)
  selection = input()
  if selection == 'no'.lower():
    typewriter("You decline the monster's help\n", 0.02)
    typewriter("You haven't got the time to help monsters\nYou choose to go alone, walking deep into theforest.", 0.02)
    going_alone_ascii()
    time.sleep(2.00);
    typewriter("You stumble in the dark and fall into a pit full of venomous snakes\n", 0.02)
    snake_ascii()
    time.sleep(2.00);
    game_over_ascii(first_name)
    final_choice_of_the_user()
  elif selection == 'yes'.lower() :
    monster_speech()    
    

def final_choice_of_the_user():
  decision = input("Do you want to play again (enter yes or no) ").lower()
  # typewriter(f"fdecision  {decision}")
  while (decision != "yes" and decision != "no"):
    decision = input("      either 'yes' or 'no' please      ").lower()
  
  if decision == 'yes':
    start_game()
  elif decision == 'no':
    # game_over_ascii(first_name)
    exit()

def game_restart(first_name):
  #ASCII for game start
  print(""" 

'##::::'##::'#######::'##::: ##::'######::'########:'########:'########::::::'######::::::'###::::'##::::'##:'########:
 ###::'###:'##.... ##: ###:: ##:'##... ##:... ##..:: ##.....:: ##.... ##::::'##... ##::::'## ##::: ###::'###: ##.....::
 ####'####: ##:::: ##: ####: ##: ##:::..::::: ##:::: ##::::::: ##:::: ##:::: ##:::..::::'##:. ##:: ####'####: ##:::::::
 ## ### ##: ##:::: ##: ## ## ##:. ######::::: ##:::: ######::: ########::::: ##::'####:'##:::. ##: ## ### ##: ######:::
 ##. #: ##: ##:::: ##: ##. ####::..... ##:::: ##:::: ##...:::: ##.. ##:::::: ##::: ##:: #########: ##. #: ##: ##...::::
 ##:.:: ##: ##:::: ##: ##:. ###:'##::: ##:::: ##:::: ##::::::: ##::. ##::::: ##::: ##:: ##.... ##: ##:.:: ##: ##:::::::
 ##:::: ##:. #######:: ##::. ##:. ######::::: ##:::: ########: ##:::. ##::::. ######::: ##:::: ##: ##:::: ##: ########:
..:::::..:::.......:::..::::..:::......::::::..:::::........::..:::::..::::::......::::..:::::..::..:::::..::........::

    """)
  first_name = input('Enter your name? ').capitalize()


####### NEIL MADE THIS BIT ########


def monster_speech():
  typewriter(
    "Monster says, 'Hi there! I\'m looking for a potion or some mushrooms to cure my poorly dog.\nI\'m a bit lost here. What are you up to?'\n", 0.02
  )
  time.sleep(2.00);
  typewriter("    'Hi monster' you say.\n    I think there might be a cure for your doggie!\n    Do you know where mushrooms are growing?\n    Else there's a secret potion recipe in my pocket.\n    Either way, I\'m lost here as well.\n\n", 0.02)
  time.sleep(5.00);
  choice_two = input(
    """Enter 'c' to ask monster to help us find the mushrooms  
Enter 'd' to offer to show monster your secret potion recipe
Enter 'e' to ask for directions.
>""")
  while (choice_two != 'c' and choice_two != 'd' and choice_two != 'e'):
    choice_two = input("    c,d or e please          ").lower()

  if choice_two == "c":
    mushroom_option()
  elif choice_two == "d":
    secret_potion()
  elif choice_two == "e":
    typewriter("'I\'m also lost too!' said the monster\n", 0.02)
    typewriter("You leave alone,\nfor you find the monster frightening and you explore the wood aimlessly.", 0.02)
    going_alone_ascii()
    typewriter("You fall down a pit full of venomous snakes\n", 0.02)
    snake_ascii()
    game_over_ascii(first_name)
    # typewriter(
    #   "\n\nYou leave alone, for you find the monster frightening and you explore the wood aimlessly.\n\n"
    # )
    #game_over()

def choicepoint() :
  choiceone = input(
    "type 'a' to befriend the monster, type 'b' to leg it   ").lower()
  while choiceone != "a" and choiceone != "b":
    choiceone = input("      either 'a' or 'b' please        ").lower()
  if choiceone == "a":
    monster_speech()
  elif choiceone == "b":
    leg_it()

    
# Function
def mushroom_option():
  typewriter("""So, you know how to make a cure with magical mushrooms.I know a place, follow me.
You follow the monster to a dark part of the forest and see a large patch of mushrooms surrounded by\na sharp, spiky fence with a gate and a sign.
The sign has a message on it
 .================================================================.
    |To gain access to these fungi you must complete 3 maths puzzles |
    |                                           /``\                 |
    |   To begin the puzzle press this button  |    |                |
    |                                           \,,/                 |                                           |
    .===============================================================.
    """, 0.02)
  time.sleep(5.00);
  mush_gate = input("\nType a if you want to press the button or\nType b to hop over the fence and ignore the sign\n>").lower()
  if mush_gate == "a":
    typewriter("\nThe sign spins around and a maths puzzle is revealed\n",0.02)
    maths_puzz1()
  if mush_gate == "b":
    typewriter("As if it would be that easy!!\nYou grab the fence to hop over it and get an huge electric shock.\nHope you have clean underwear at home.\nThe monster laughs and presses the button for you\n",0.02)
    typewriter("The sign spins around and a maths puzzle is revealed\n", 0.02)
    time.sleep(5.00);
    maths_puzz1()
#####Maths puzzles funnctions####
def maths_puzz1():
  tries=2
  maths_answer1 = input("~~Type an even prime number.~~\n>")
  while maths_answer1 != "2" and tries<4:
    typewriter(f"Wrong answer, you are on try {tries} of 3 attempts\nTry again\n",0.02)
    tries+=1
    maths_answer1 = input("~~Type an even prime number.~~\n>")
  if maths_answer1=="2":
    typewriter("That is the correct answer\nNext question\n",0.02)
    maths_puzz2()
  else:
    typewriter(""""You have failed the maths test
What a dummy.
A hole appears under you and you fall into a pit of angry venomous snakes.""", 0.03)
    snake_ascii()
    game_over_ascii(first_name)
    final_choice_of_the_user()

def maths_puzz2():
  tries=2
  maths_answer2 = input("~~If I add 6 to 11, I get 5. What am I looking at?~~\n>").lower()
  while maths_answer2 != "clock" and maths_answer2!= "aclock" and maths_answer2!= "a clock" and tries<4:
    typewriter(f"Wrong answer, you are on try {tries} of 3 attempts\nTry again\n", 0.02)
    tries+=1
    maths_answer2 = input("~~If I add 6 to 11, I get 5. What am I looking at?~~\n>").lower()
  if maths_answer2 =="clock":
    typewriter("That is the correct answer\nNext question\n",0.02)
    maths_puzz3()
  if maths_answer2 =="a clock":
    typewriter("That is the correct answer\nNext question\n",0.02)
    maths_puzz3()
  if maths_answer2 =="aclock":
    typewriter("That is the correct answer\nNext question\n", 0.02)
    maths_puzz3()
  else:
    typewriter(""""You have failed the maths test.
What a dummy.
A hole appears under you and you fall into a pit of angry venomous snakes.""", 0.02)
    snake_ascii()
    game_over_ascii(first_name)
    final_choice_of_the_user()
    
def maths_puzz3():
  tries=2
  maths_answer3=input("~~A grandfather,2 fathers and 2 sons go to the cinema and everyone bought one ticket each.\nHow many tickets were bought?~~\n>")
  while maths_answer3 !="3" and tries<4:
    typewriter(f"Wrong answer, you are on try {tries} of 3 attempts\nTry again",0.02)
    tries+=1
    maths_answer3 = input("\n~~A grandfather,2 fathers and 2 sons go to the cinema and everyone bought one ticket each.\nHow many tickets were bought?~~\n>")
  if maths_answer3 == "3":
    typewriter("That is the correct answer\n", 0.02)
    ending_finish()
  else:
    typewriter("""You have failed the maths test
What a dummy.
A hole appears under you and you fall into a pit of angry venomous snakes.""", 0.02)
    snake_ascii()
    game_over_ascii(first_name)
    final_choice_of_the_user()

#
# #This is the good ending where you all survive
#
def ending_finish():
  typewriter("""You successfully create the cure and give it to the monster's sick dog.
The dog leaps up and licks you on the face in excitement.
The monster, equally as excited also leaps up and licks you on the face sending you to the floor with a bump
and a wet face.
  'Thank you for curing my dog' says the monster.
  'Can I buy you a drink at my favourite pub The Frolicking Maggot?
\n""", 0.02)
  happy_ending = input("Type 'a' to join the monster in the pub or\nType 'b' to head home, you've had enough excitement for the day\n>").lower()
  tries=1
  while happy_ending!="a" and happy_ending!="b":
        typewriter("That is not a valid option",0.02)
        tries+=1
        typewriter(f"This was attempt number {tries} to type a or b. Try again",0.02)
        happy_ending=input("Type a to join the monster in the pub or\nType b to head home, you've had enough excitement for the day\n>").lower()

  if happy_ending=="a":
    typewriter(""""
      .======================================.
      | ___ ___ ___               _   _   _  |
      | \_/ \_/ \_/ C|||C|||C||| |-| |-| |-| |
      | _|_ _|_ _|_  ||| ||| ||| |_| |_| |_| |
      '===================================== '
                 =====================                
                |The Frolicking Maggot |      
           .:.   =====================                           
          C|||'                             
        ___|||______________________________
       [____________________________________]
        |   ____    ____    ____    ____   | 
        |  (____)  (____)  (____)  (____)  | 
        |  |    |  |    |  |    |  |    |  | 
        |  |    |  |    |  |    |  |    |  |  
        |  |    |  |    |  |    |  |    |  | 
        |  |____|  |____|  |____|  |____|  | 
        |  I====I  I====I  I====I  I====I  | 
        
        You head off to the pub with the monster and his dog, and become firm friends
        THE END
              """,0.02)
  if happy_ending == "b":
    typewriter("""
        `'::.
    _________H ,%%&%,
   /\     _   \%&&%%&%
  /  \___/^\___\%&%%&&
  |  | []   [] |%\Y&%'
  |  |   .-.   | ||  
~~@._|@@_|||_@@|~||~~~~~~~~~~~~~
     `''') )'''`""",0.02)
    typewriter("You head off home after a long, interesting day.\nYou swap numbers with the monster so you can meet up again with your new friend.\n", 0.02)
###### alternative ending to test function########
  # play_again = input(
  #   """Would you like to play again?\nType y to start again\nOr n to end the game\n>"""
  # ).lower()
  # while play_again != "y" and play_again != "n":
  #   typewriter("That is not a valid option")
  #   play_again = input("Would you like to play again?\n>").lower()
  # if play_again == "y":
  start_again()
  # if play_again == "n":
  #   typewriter(f"Thank you for playing {first_name}\nGOODBYE")
  #   exit()

def start_again():
  decision = input("\nDo you want to play again?\nType yes or no\n> ").lower()
  typewriter(decision, 0.02)
  while (decision != "yes" and decision != "no"):
    decision = ("either yes or no please   ").lower()
  
  if decision == "yes":
    start_game()
  elif decision == "no":
    exit()
  else :
    exit()



####### IMA MADE THIS BIT ########


def secret_potion():
  typewriter("""I see you have a secret potion recipe\nFollow me I know a goblin that can sell us the ingredients.
You follow the monster through a pathway full of different kinds of vegetable and fruits.\nAs you go along you meet a goblin holding a sign saying
    
                       ( O O )        
       |---------ooO-----(_)-----ooO--------------------|
       |(To make the secret potion you will have to get |
       | the following riddles correct to collect the   |
       | accurate ingredients. If you fail to do so the |
       | potion will explode 💥)                        |
       |------------------Ooo---------------------------|
                       |__||__|        
                        ||  ||         
                       ooO  Ooo        

As you enter the goblins'kingdom of potions you see a huge bowl where all your ingredients will be mixed.\nYou are quite lucky that this potion won't require many ingredients 😉
        
    (\
     \ \
 __    \/ ___,.-------..__        __
//\\ _,-'\\               `'--._ //\\
\\ ;'      \\                   `: //
 `(          \\                   )'
   :.          \\,----,         ,;
    `.`--.___   (    /  ___.--','
      `.     ``-----'-''     ,'
         -.               ,-
           `-._______.-'
  """, 0.02)
  
  
  
  riddle_1 = input("What must be broken before it can be used?\n>").lower()
  tries = 0
  while riddle_1!= "egg" and riddle_1!="an egg" and tries < 3:
    print("You got the wrong ingredient. You have 3 more chances")
    tries += 1
    print(f"You have made {tries} attempts / 3")
    riddle_1 = (input("What must be broken before it can be used?\n>")).lower()
  
  if riddle_1 == "egg" or riddle_1 == "an egg":
    print(
      "Well Done! You got the first ingredient for the secret potion correct. We need one more ingredient to make the potion"
    )
  # if riddle_1 == "an egg":
  #   print(
  #     "Well Done! You got the first ingredient for the secret potion correct. We need one more ingredient to make the potion"
  #   )
  else:
    restart_game = input("BOOM!!Your potion has exploded 💥. Game over 💀. Do you want to restart again?\nType yes/no\n>").lower()
  
    if restart_game == "yes":
      start_game()
    else:
      print("BOOM!!Your potion has exploded 💥. Game over 💀")
      typewriter("""
       ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
    ███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀
    ██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼
    ██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀
    ██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼
    ███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄
    ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
    ███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼
    ██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼
    ██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼
    ██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼
    ███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄
    ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼████▄┼┼┼▄▄▄▄▄▄▄┼┼┼▄████┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼▀▀█▄█████████▄█▀▀┼┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼┼┼█████████████┼┼┼┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼┼┼██▀▀▀███▀▀▀██┼┼┼┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼┼┼██┼┼┼███┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼┼┼█████▀▄▀█████┼┼┼┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼┼┼┼███████████┼┼┼┼┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼▄▄▄██┼┼█▀█▀█┼┼██▄▄▄┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼▀▀██┼┼┼┼┼┼┼┼┼┼┼██▀▀┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼

     """,0.02)
    exit()
  typewriter("""
   (       "     )  APPLYING WHAT I LEARNED   
    ( _  *         FROM THE HARRY POTTER BOOKS
       * (     /      \    ___                
          "     "        _/ /                 
         (   *  )    ___/   |                 
           )   "     _ o)'-./__               
          *  _ )    (_, . $$$                 
          (  )   __ __ 7_ $$$$                
           ( :  { _)  '---  $\                
      ______'___//__\   ____, \               
       )           ( \_/ _____\_              
     .'             \   \------''.            
     |='           '=|  |         )           
     |               |  |  .    _/            
      \    (. ) ,   /  /__I_____\             
  snd  '._/_)_(\__.'   (__,(__,_]             
      @---()_.'---@  
  """, 0.02)
  
  riddle_2 = (input(
    "What vegetable is the most fun to be around and the one everyone wants to hangout with?\n>"
  )).lower()
  tries_1 = 0
  while riddle_2 != "fungi" and riddle_2!= "a fungi" and tries_1 < 3:
    typewriter("You got the wrong ingredient. You have 3 more chances\n",0.02)
    tries_1 += 1
    typewriter(f"You have made {tries_1} attempts / 3\n",0.02)
    riddle_2 = (input(
      "What vegetable is the most fun to be around and the one everyone wants to hangout with?\n>"
    )).lower()
  
  if riddle_2 == "fungi":
    typewriter(
      "Well Done! You got the second ingredient for the secret potion correct.\nYou have successfully made the potion and doggie can be saved. Yahooo!\n", 0.03)
    ending_finish()
  if riddle_2 =="a fungi":
    typewriter(
     "Well Done! You got the second ingredient for the secret potion correct.\nYou have successfully made the potion and doggie can be saved. Yahooo!", 0.03) 
    ending_finish()
  else:
    play_again = input("BOOM!! Your potion has exploded 💥. Game Over 💀!, Do you want to restart again?\nType yes/no\n>")
    if play_again == "yes":
      start_game()
    else:
      typewriter("BOOM!!Your potion has exploded 💥. Game over 💀",0.02)
      print("""
              ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
    ███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀
    ██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼
    ██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀
    ██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼
    ███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄
    ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
    ███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼
    ██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼
    ██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼
    ██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼
    ███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄
    ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼████▄┼┼┼▄▄▄▄▄▄▄┼┼┼▄████┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼▀▀█▄█████████▄█▀▀┼┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼┼┼█████████████┼┼┼┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼┼┼██▀▀▀███▀▀▀██┼┼┼┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼┼┼██┼┼┼███┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼┼┼█████▀▄▀█████┼┼┼┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼┼┼┼███████████┼┼┼┼┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼▄▄▄██┼┼█▀█▀█┼┼██▄▄▄┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼▀▀██┼┼┼┼┼┼┼┼┼┼┼██▀▀┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼


      """, 0.02)
    
    
    exit()  
  print("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠒⠉⢀⣀⣤⣤⣄⣀⠈⠑⠢⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠋⢀⣴⣾⠿⠛⠛⠛⢛⠿⢿⣶⣤⣀⠉⠒⠤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⠁⢠⣾⠟⠁⠀⠀⠀⠀⠀⡄⠀⠈⠙⠿⣷⣦⣤⣀⣈⠉⠀⠒⠢⠤⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠜⠁⣰⣿⢏⠖⠐⠢⡀⠀⠀⠀⠈⠒⠒⠒⠊⠀⠉⠙⠛⠿⠿⣷⣶⣦⣤⣄⠈⠙⠢⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠔⠁⣀⣼⡿⢣⠎⠀⠀⠀⣇⠀⠀⠀⠀⠀⠀⠀⢀⠔⠋⠉⠉⠓⢢⡀⠀⢹⠛⣿⢿⣦⡀⠙⡄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢠⠞⠁⢠⣾⡿⢋⠜⠁⠀⠀⠀⢀⠏⠀⡴⠚⠙⠒⡄⠀⠈⢦⠀⠀⠀⠀⢀⡇⣰⠃⠀⠀⢥⢻⣷⠀⢹⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⠔⠁⢀⣼⡿⡏⠀⢸⡀⠀⠀⢀⡠⠞⠀⠘⣄⠀⠀⢀⠟⠀⠀⠀⠙⠂⠤⠤⣮⠜⠁⣀⡤⠔⠯⢿⢿⠀⢸⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡰⠋⢀⣴⣿⣋⠴⠁⠀⠀⠉⠀⠈⠁⠀⠀⠀⠀⠈⠁⠒⠉⠀⠀⠀⠀⣀⣠⡴⠊⠁⢐⡞⠁⠀⠀⢀⣾⡿⠀⡼⠀⠀⠀⠀
⠀⠀⠀⠀⣰⠁⢠⣿⠟⠀⠀⠀⠀⢠⠖⠐⢦⠀⠀⠀⠀⣀⢀⣀⣠⡤⠴⠒⠢⠈⠉⠀⠈⠀⠀⠀⢨⣣⣀⣤⣶⣿⠟⠁⡰⠃⠀⠀⠀⠀
⠀⠀⠀⠀⡏⠀⣿⡏⠉⢢⠀⠀⠀⠸⢤⣠⠞⠀⣀⡤⢺⡁⠀⠈⡿⠃⠀⣀⣰⡷⣿⣟⣗⣲⣭⠭⠿⠟⠛⠋⠉⢀⡤⠚⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣇⠀⣿⣇⢀⡜⠀⠀⠀⠀⠀⠀⣠⠾⠁⠀⢉⡻⣶⣾⣶⣿⠿⠛⠛⠋⠉⣿⡇⠀⡤⠤⠤⠐⠒⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠘⡀⠘⢿⣧⣀⠀⠀⠀⠀⠀⡼⠁⣀⡤⣶⣾⣿⣿⠋⠁⠀⠀⠀⠀⠀⠀⢻⣇⠀⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠙⢄⠀⠙⠿⢿⣶⣶⣖⣾⡿⠿⠟⠛⠉⠁⢸⢹⠀⠀⠀⠀⠀⠀⠀⠀⢸⣸⠀⢰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠉⠒⢤⣄⡀⢀⣀⠀⠠⠤⠔⠒⢸⠀⢸⢸⠀⠀⡠⠀⠀⠀⠲⣄⠘⣿⡇⠘⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⡴⠒⠉⣉⣈⠉⠑⢦⡀⠀⠀⠀⠀⢸⠀⢸⣾⢀⠎⠀⠀⠀⠀⠀⠈⠳⢿⣷⠀⢱⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣠⠔⠚⠁⣀⣴⢟⣋⠙⠻⣦⡀⠑⢄⠀⠀⠀⢸⠀⣸⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠘⡿⡇⠈⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⡞⠀⣠⡶⢛⣋⠠⡁⢈⠗⣠⢼⢷⣄⡀⠑⡄⠀⡇⠀⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣷⠀⢰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⠀⢸⣿⡷⢧⣀⠇⠀⠀⠀⠑⠚⠀⠙⢷⡄⢸⢰⠃⢠⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡿⡇⠘⡆⠀⠀⣠⠤⠒⠒⠒⠂⠤⣄⠀⠀
⠈⡄⠘⢷⣄⣀⣀⣀⣰⣏⡹⠀⠀⠀⢀⣼⠇⢸⠛⠀⣼⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⢧⠀⢃⡴⠊⢀⣠⡶⣶⣶⢶⣤⣀⠉⢲
⠀⠙⠦⣀⣈⠉⠉⢹⡏⣿⠛⠶⠶⠶⠟⠁⣠⠎⡇⢀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠈⠀⣰⢿⣗⡄⠑⠊⠀⠉⣻⡇⠀
⠀⠀⠀⠀⢈⠏⠀⣾⠀⣿⠀⠠⠀⠀⠐⠚⠁⢸⠁⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⡇⠀⠘⣿⣄⣈⣐⣭⣦⣴⠾⠋⢀⡼
⠀⠀⠀⠀⡞⠀⣼⠃⢰⡇⠀⡇⠀⠀⠀⠀⠀⢸⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⢰⡤⣀⡈⠉⢉⡟⠹⣧⠀⢰⠋⠀
⠀⠀⠀⢰⠁⢰⠏⠀⢸⡇⠀⡇⠀⠀⠀⠀⠀⢸⡀⢸⣸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⡇⢸⠃⠀⢸⠁⢸⡇⠀⠹⣇⠀⡇⠀
⠀⠀⠀⡟⠀⣿⠀⠀⢘⡇⠀⡇⠀⠀⠀⠀⠀⠀⡇⠈⢿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣻⠀⢸⠀⠀⠸⡆⠘⣧⠀⠀⣿⠀⡇⠀
⠀⠀⠀⢷⠀⢿⣄⣀⣼⠇⢀⡇⠀⠀⠀⠀⠀⠀⠸⡄⠘⢿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣰⣿⠇⢠⠇⠀⠀⠀⢣⡀⠹⠦⠾⠋⢀⠇⠀
⠀⠀⠀⠈⢦⡀⠉⠉⠁⣀⠞⠀⠀⠀⠀⠀⠀⠀⠀⠙⢆⡀⠙⠿⣷⣶⣤⣤⣤⣤⣴⣶⣿⠟⠁⣠⠎⠀⠀⠀⠀⠀⠑⠤⠤⠤⠴⠋⠀⠀
⠀⠀⠀⠀⠀⠈⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠢⢄⣀⠈⠉⠉⠉⠉⠉⢁⣀⡤⠚⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""", 0.02)
  ending_finish()

#ASCII for game start
typewriter(""" 
' 
 ##::::'##::'#######::'##::: ##::'######::'########:'########:'########::::::'######::::::'###::::'##::::'##:'########:
#  ###::'###:'##.... ##: ###:: ##:'##... ##:... ##..:: ##.....:: ##.... ##::::'##... ##::::'## ##::: ###::'###: ##.....::
#  ####'####: ##:::: ##: ####: ##: ##:::..::::: ##:::: ##::::::: ##:::: ##:::: ##:::..::::'##:. ##:: ####'####: ##:::::::
#  ## ### ##: ##:::: ##: ## ## ##:. ######::::: ##:::: ######::: ########::::: ##::'####:'##:::. ##: ## ### ##: ######:::
#  ##. #: ##: ##:::: ##: ##. ####::..... ##:::: ##:::: ##...:::: ##.. ##:::::: ##::: ##:: #########: ##. #: ##: ##...::::
#  ##:.:: ##: ##:::: ##: ##:. ###:'##::: ##:::: ##:::: ##::::::: ##::. ##::::: ##::: ##:: ##.... ##: ##:.:: ##: ##:::::::
#  ##:::: ##:. #######:: ##::. ##:. ######::::: ##:::: ########: ##:::. ##::::. ######::: ##:::: ##: ##:::: ##: ########:
# ..:::::..:::.......:::..::::..:::......::::::..:::::........::..:::::..::::::......::::..:::::..::..:::::..::........::

# """, 0.01)
#first prompt when we run the file
first_name = input('Enter your name? ').capitalize()

start_game()