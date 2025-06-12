#Day-1 Python: Concatination,input function ,veriables,switching veriables,giving space 

print("hello")
print("Hello world!\nHellow world!") #Back slash(\n) to write the words in two different lines 
print("Hellow "+ "world") #String concatination 
print("String concatination done with the '+' sign")

#Learning to write input function
input("What is your name? :" )
print("Hello " + input("what is your name?: "))
print(len(input("what is ur name? "))) #calculates the length of the the string 

#Veriables in Python 
p = input("What is ur name? ")
length= len(p)
print(length)

# Swithching variables 
a = input("a:")
b = input("b:")
c = a 
a = b
b = c 
print(a)
print(b)

#Project 1 :Band name generator 
city_name = input("What is name of the city you grew up?\n ")
pet_name = input("What is your pet name?\n")

result = print("Your band name could be " + city_name + " " + pet_name )
print(result)

# Project 3 : Tresure Island 
 
print('''***********************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                                       
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
print("Wlcome to the Tresure Island Game!")
print("Your mission is to find the tresure")
choice_1 = input('You\'re at a crossroad,where do you want to go? Type "left" or "right".').lower()

if choice_1 == "left":
    choice_2 =input('You\'ve come to a lake.There is an island in the middle of the lake.Type "Wait" to wait for a boat,Type "swim" to swim across')
    if choice_2 == "wait":
        choice_3 = input("Great move,Now you have arrived at the island unharmed.There is a house with 3 doors. one red,one yellow and one blue.Which color do you want to choose").lower()
        if choice_3 == "red":
            print("It's a room full of fire.Game Over!")
        elif choice_3 == "yellow":
            print("Congrats,you found the tressure! You Won!")
        elif choice_3 == "blue":
            print("You chose the room of beasts.Game over!")
        else:
            print("Door doesn't exist,Game Over!")
    else:
       print("You got attacked by an angry trout.Game Over!")  
else:
    print("You fell into a hole,Game Over!")