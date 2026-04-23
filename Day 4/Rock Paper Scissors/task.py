import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
art = [rock, paper, scissors]
art_names = ["Rock", "Paper", "Scissors"]

print("Welcome to the Rock Paper Scissors game!")
your_pick = int(input("What do you choose?  0- rock, 1 - paper, or 2 - scissors: "))
#generate computer pick
computer_pick = random.randint(0, 2)
print("you picked #", your_pick, art_names[your_pick], art[your_pick],
      " And computer picked", computer_pick, art_names[computer_pick], art[computer_pick])


if your_pick >= 3 or your_pick < 0:
    print("Choose 1,2, or 3 ")
elif your_pick == computer_pick:
   #print("You picked " + names[your_pick] + " and the computer picked " + names[computer_pick])
    print("It's a tie!")
elif your_pick == 0 and computer_pick ==2:
    print("You win!")
elif your_pick == 2 and computer_pick == 0:
    print("You lose!")
elif your_pick > computer_pick:
    print("You win!")
elif computer_pick > your_pick:
    print("You lose!")
