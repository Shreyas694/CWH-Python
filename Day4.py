#Randomization in Python

import random # Module is a part of system eg tyre of the car
value = random.uniform(1,10)
print(value)
value = random.randint(1,6)
print(value)
random_integer = random.randint(1,10)
print(random_integer)

value = random.randint(1,6)

greeting = ['Hellow','Hi','Hey','Howdy','Hola']
value = random.choice(greeting)
print(value,""'Shreyas!')

random_float = random.random() * 5
print(random_float)

love_score = random.randint(1,100)
print(f"Your love score is {love_score}")

# Heads or Tails 
import random

random_side = random.randint(0,1)
if random_side == 1:
    print("Heads")
else:
    print("Tails")

# Python Lists : Lists are the data structures allows to organize and store the data 
#Lists are the set of square brackets stores related many items separated by the commas 
fruits = ["cherry", "apple","mango"]
print(fruits[-1]) # pulling out the last item in the list 
fruits [1] = "banana" # changing the item at 1
print(fruits)
fruits.append("sapota") # adds a new item at the end of the list 
print(fruits)
fruits.extend(["Jack fruits","dragen fruit"]) # adds the additioal items to the lists 
print(fruits)

# Selecting the random name,who will pay the bill 

names_string = input("Give me everybody's names,separated by the comma.")
names = names_string.split(",")
num_item = len(names)
print(num_item)
import random
random_choice= random.randint(0,num_item-1)
person_pay = names[random_choice]
print(f"{person_pay} is going to buy the meal today!")

# Short code 

person_pay = random.choice(names)
print(f"{person_pay} is going to buy the meal today!")
print(person_pay + "is going to buy the meal today!")

#Nested List 

fruits_1 = ["Strawberry","Nectarines","Apples","Grapes","Peaches","Pears"]
vegetables = ["Spinach","Kale","Tomatoes","Celery","Potatoes"]
dirty_dozen = [fruits_1,vegetables]
print(dirty_dozen)

# Tresure Map Exercise

row1 = [" "," "," "]
row2 = [" "," "," "]
row3 = [" "," "," "]
map = [row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the tresure? ")
horizontal = int(position[0])
vertical = int(position[1])

selected_row = map[vertical-1]
selected_row[horizontal-1] = "X"

#Python Project-4: Rock,Paper and Scissor Game
# Rules: 
# Rock(0) wins against the scissors(2)
# Scissors(2) win against the paper(1)
# Paper(1) wins against the rock(0)

rock = '''
    _______
---'   ____)
      (_)
      (_)
      ()
---.(_) '''

paper = '''_______
---'    ___)___
           ______)
          _______)
         _______)
---.) '''

scissors = '''_______
---'   ___)___
          ______)
       __________)
      ()
---.(_) '''


game_images = [rock,paper,scissors]

user_choice = int(input("What do you choose? Type 0 for Rock,1 for Paper or 2 for Scissors.\n"))
if user_choice >=3 or user_choice <0:
    print("You typed invalid number,you loose!")
else:
   print(game_images[user_choice])

   import random 
   computer_choice = random.randint(0,2)
   print("Computer chose:")
   print(game_images[computer_choice])


   if user_choice == 0 and computer_choice == 2:
    print("You won!")
   elif computer_choice == 0 and user_choice == 2:
        print("You loose")
   elif user_choice > computer_choice:
        print("You Won!")
   elif computer_choice > user_choice:
        print("You lose!")
   elif computer_choice == user_choice:
        print("It's draw!")