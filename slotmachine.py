import random
import time
import os
balance =0.0
def quit_game():
  os.system('clear')
  print("Thanks for playing")
  print("----------------------------------------------------")
def home():
  os.system('clear')
  print("----------------------------------------------------")
  print("--------------------Slot House----------------------")
  print("----------------------------------------------------")
  print(f"Your current Balance is: ${balance}")

  print("A.Deposit Money")
  print("B.Start the Game")
  print("C.Quit the Game")

  print("----------------------------------------------------")
  choice=input("Enter Your Choice : ")
  print("----------------------------------------------------")
  if(choice.lower()=='a'):
    ask_deposit()
    os.system('clear')
    home()
  elif(choice.lower()=='b'):
    main()
    c=input("continue playing?? (Y/N)")
    if c.lower()=='y':
      home()
    else:
      quit_game()
  elif(choice.lower()=='c'):
    quit_game()
  else :
    print("Invalid Choice, Please try again")
    home()

def ask_deposit():
  global balance
  while True:
    deposit=input("Enter the Amt to be DESPOSITED: $")
    if(deposit.isdigit()):
      deposit =float(deposit)
      if(deposit>0):
        balance+=deposit
        print(f"Your current balance is:${balance}")
        break;
      else:
        print("Enter a positive number Dumbass!!")
    else:
      print(f"Does this seem like a number to you IDIOT ::{deposit}")
def main():
    deflist = "🍒🍀💎⭐🍒🍀💎⭐🍒"
    inlist1 = list(deflist)
    inlist2 = list(deflist)
    inlist3 = list(deflist)
    random.shuffle(inlist1)
    random.shuffle(inlist2)
    random.shuffle(inlist3)
    complist = [inlist1, inlist2, inlist3]
    os.system('clear')
    global balance
    print(f"Your current balance is:${balance}")
    bet = input("Enetr your bet: $")
    while not bet.replace('.', '', 1).isdigit() or float(bet) > float(balance) or float(bet) < 0:
        print("Insufficient Balance or invalid bet")
        bet = input("Enetr your bet: $")
    bet = float(bet)
    i = game(complist)
    points(i, complist, bet)

def game(complist):
    os.system('clear')
    print("----------------------------------------------------")
    n = int(input("Enter the number of seconds to stop after ---> "))
    i = 0
    list_len = len(complist[0])
    while n > 0:
        i = (i + 1) % list_len
        print(f"----------------------------")
        print(f"|  {complist[0][i]}  |  {complist[1][i]}  |  {complist[2][i]}  |")
        time.sleep(1)
        n = n - 1
    return i
def points (i,complist,bet):
  global balance
  balance=balance-int(bet)
  if complist[0][i]==complist[1][i] or complist[0][i]==complist[2][i] or complist[2][i]==complist[1][i]:
    multiplier=1.0
    bet *= multiplier
    print("Your winnings is : $", bet)
  elif complist[0][i]==complist[1][i] and complist[1][i]==complist[2][i]:
    multiplier=2.0
    bet *= multiplier
    print("Your winnings is : $", bet)
  else:
    multiplier=0
    bet *= multiplier
    print("You lost your bet")


  balance += bet
  print("----------------------------------------------------")
  print(f"Your new balance is: ${balance}")
  print("----------------------------------------------------")

home()
