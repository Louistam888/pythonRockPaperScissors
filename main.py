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

#Write your code below this line 👇

userChoice = input("Enter rock, paper, or scissors ").lower()

computerChoices = [rock, paper, scissors]

if userChoice == "rock": 
  print(f"\n You chose rock \n {rock}")
elif userChoice == "paper":
  print(f"\n You chose paper \n {paper}")
elif userChoice == "scissors":
  print(f"\n You chose scissors \n {scissors}")
else:
  print("incorrect entry")

computerPick = random.choice(computerChoices)
print(f"\n Computer chose \n {computerPick}")

if userChoice == "rock" and computerPick == paper: 
  print(f"\n Computer wins.")
elif userChoice == "rock" and computerPick == scissors:
  print(f"\n You win.")
elif userChoice == "paper" and computerPick == rock:
  print(f"\n You win.")
elif userChoice == "paper" and computerPick == scissors:
  print(f"\n Computer wins.")
elif userChoice == "scissors" and computerPick == rock:
  print(f"\n Computer wins.")
elif userChoice == "scissors" and computerPick == paper:
  print(f"\n You win.")
else:
  print(f"\n Tie game.")
