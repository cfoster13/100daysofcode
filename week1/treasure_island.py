print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

print("You've crash landed on an island, and entered a cave, there are two paths...")
path_direction = input("Do you go left or right?: ")

if path_direction == "right" or path_direction == "Right":
    print("You walk down the path, suddenly the light starts to disappear...")
    print("You cannot see where you are going")
    print('''                          
                            
    
                 ______ ./
                (      -. ____
               (              )
                '-._\_\___.---'
''')
    print("You fall down a hole.") # PRINT A HOLE PICTURE

elif path_direction == "left" or path_direction == "Left":
    print("Going deeper into the cave, there are faint voices and you come across a pool of water...")
    swim_choice = input("Do you swim across to the other side, or wait to see where the voices are coming from? [Enter wait or swim]: ")
    
    if swim_choice == "swim" or swim_choice == "Swim":
        print("You start swimming across, but something grabs your leg from underwater...")
        print('''                                              ,--,  ,.-.
                ,                   \,       '-,-`,'-.' | ._
               /|           \    ,   |\         }  )/  / `-,',
               [ '          |\  /|   | |        /  \|  |/`  ,`
               | |       ,.`  `,` `, | |  _,...(   (      _',
               \  \  __ ,-` `  ,  , `/ |,'      Y     (   \_L\
                \  \_\,``,   ` , ,  /  |         )         _,/
                 \  '  `  ,_ _`_,-,<._.<        /         /
                  ', `>.,`  `  `   ,., |_      |         /
                    \/`  `,   `   ,`  | /__,.-`    _,   `\
                -,-..\  _  \  `  /  ,  / `._) _,-\`       \
                 \_,,.) /\    ` /  / ) (-,, ``    ,        |
                ,` )  | \_\       '-`  |  `(               \
               /  /```(   , --, ,' \   |`<`    ,            |
              /  /_,--`\   <\  V /> ,` )<_/)  | \      _____)
        ,-, ,`   `   (_,\ \    |   /) / __/  /   `----`
       (-, \           ) \ ('_.-._)/ /,`    /
       | /  `          `/ \\ V   V, /`     /
    ,--\(        ,     <_/`\\     ||      /
   (   ,``-     \/|         \-A.A-`|     /
  ,>,_ )_,..(    )\          -,,_-`  _--`
 (_ \|`   _,/_  /  \_            ,--`
  \( `   <.,../`     `-.._   _,-`
   `                      ``` ''')
        print("You're being dragged below and you start to drown.") # PRINT A MONSTER
    
    elif swim_choice == "wait" or swim_choice == "Wait":
        print("The voices become clearer...")
        print("Someone is whispering to you that there are different coloured rocks")
        print('''           ,
        .--')
       /    /
      |    /
   /`.\   (_.'\
   \          /
    '--. .---'
      ( " )
       '-'
                ,
                 \`-,      ,     =-
             .-._/   \_____)\
            ("              / =-
             '-;   ,_____.-'       =-
              /__.'


       .-.
      ( " )
   /\_.' '._/\
   |         |
    \       /
     \    /`
   (__)  /
jgs`.__. ''')
        print("Pick the right coloured rock and you will be rewarded...")
        print("Otherwise you will suffer the consequences") # PRINT A GHOST

        coloured_rock = input("Which coloured rock do you choose: red, blue or yellow? ")
        if coloured_rock == "red" or coloured_rock == "Red": # PRINT A SKULL
            print("That wasn't the correct choice...")
            print("Red represents blood and death")
            print('''
     |     '       /  |    |             /  |
     /__      ___ (  /     /__   Y  __  (  _/
     \\--`-'-|`---\\ |     \`--`-'-|`---\\/
      |' _/   ` __/ /       |'__/   ` __/ |
      '._  W    ,--'        '-.   w   ,--/
         |_:_._/              |'_._._/  /
                              |________/
                                                ''')
            print("Now you will suffer")
        
        elif coloured_rock == "blue" or coloured_rock == "Blue":
            print("Wrong choice... ") # PRINT THE OCEAN
            print("Blue represents the ocean and how you will die...")
            print("Is by drowning...")
        
        elif coloured_rock == "yellow" or coloured_rock == "Yellow":
            print("You have chosen victory...") # PRINT A CHEST
            print("Yellow stands for gold")
            print("Here is your treasure...")
            print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/________
*******************************************************************************''')
            
