'''Vending Machine
IU Summer 2022
Kristin Scott'''

import random


def return_change(change_total):
  change_msg="Your change is: \n"
  amt_to_return=change_total

  if amt_to_return > 10:
    amt_to_return -=10
    change_msg = change_msg + "a ten dollar bill\n"
  if amt_to_return > 5:
    amt_to_return -=5
    change_msg = change_msg + "a five dollar bill\n" 
  while amt_to_return >= 1:
    amt_to_return -=1
    change_msg = change_msg + "a one dollar bill\n"
  if amt_to_return >= .5:
    amt_to_return -=.5
    change_msg = change_msg + "one fifty cent coin\n"
  if amt_to_return >= .25:
    amt_to_return -=.25
    change_msg = change_msg + "a quarter\n"
  while amt_to_return >= .1:
    amt_to_return -=.1
    change_msg = change_msg + "a dime\n"
  if amt_to_return >= .05:
    amt_to_return -=.05
    change_msg = change_msg + "a nickel\n"
  while amt_to_return >= .01:
    change_msg = change_msg + "a penny\n"
    amt_to_return -=.01
    
  print(change_msg)
  

def payment(owed,cur,quant):
  pmnt=0
  still_owed=0
  
  if cur.upper().strip()=="A":
      pmnt=20*quant
  elif cur.upper().strip()=="B":
      pmnt=10*quant
  elif cur.upper().strip()=="C":
      pmnt=5*quant
  elif cur.upper().strip()=="C" or cur.upper().strip()=="E":
      pmnt=quant
  elif cur.upper().strip()=="F":
      pmnt=.5*quant
  elif cur.upper().strip()=="G":
      pmnt=.25 * quant
  elif cur.upper().strip()=="H":
      pmnt=.1*quant
  elif cur.upper().strip()=="I":
      pmnt=.05*quant
  elif cur.upper().strip()=="J":
      pmnt=.01*quant

    
  #check to see if pmnt covered the amount owed
  still_owed=owed-pmnt

  
  if pmnt==owed:
    print("Please pick up your snack below. Have a nice day!")
    
    
  elif still_owed > 0:  
      print("Amount due=", "{:.2f}".format(still_owed))
      print("--------------------------")
      currency=input("Please enter the letter to indicate the currency you will you be using. \nBILLS:\nA. \t$20\nB. \t$10 \nC.\t$5 \nD. \t$1 \nCOINS: \nE. \t1.00 \nF.\t.50 \nG.\t.25 \nH.\t.10 \nI.\t.05 \nJ.\t.01\n    ***")
  
      quant_currency=int(input("Enter quantity of this currency. \n"))

      payment(still_owed,currency,quant_currency)
    
  elif still_owed < 0:
      still_owed= 0-still_owed
      return_change(still_owed)
      #print("Your change is ", ("{:.2f}".format(still_owed)))
      print("Please take your change and pick up your snack below. Have a nice day!")
      still_owed=0
      









#declaring variables for items in machine
pringles=5 #a
pringles_Q=random.randrange(10)
pretzels=5 #b
pretzels_Q=random.randrange(10)
sunchips=5 #c
sunchips_Q=random.randrange(10)
cheetos=5 #d
cheetos_Q=random.randrange(10)
funyuns=5 #e
funyuns_Q=random.randrange(10)
doritos=5 #f
doritos_Q=random.randrange(10)
kitkat=5 #g
kitkat_Q=random.randrange(10)
reeses=5 #h
reeses_Q=random.randrange(10)
mandms=5 #i
mandms_Q=random.randrange(10)
cookies=5 #j
cookies_Q=random.randrange(10)

place_order=True
while place_order:

  selection_made=False
  
  print("-----------------------")
  print("Welcome to the ~Snack Shack~")
  print("A. Pringles \t1.00 \tQuantity available: ",pringles_Q)
  
  print("B. Pretzels\t\t .75\tQuantity available: ",pretzels_Q)
  print("C. Sun Chips\t .80\tQuantity available: ",sunchips_Q)
  print("D. Cheetos \t\t .75\tQuantity available: ",cheetos_Q)
  print("E. Funyuns\t\t .75 \tQuantity available: ",funyuns_Q)
  print("F. Doritos\t\t .75\tQuantity available: ",doritos_Q)
  print("G. Kit Kat \t\t1.20\tQuantity available: ",kitkat_Q)
  print("H. Reeses \t\t1.20\tQuantity available: ",reeses_Q)
  print("I. M & M's\t\t1.20\tQuantity available: ",mandms_Q)
  print("J. Cookies \t\t1.00 \tQuantity available: ",cookies_Q)
  
  
  
  
  
  
  print("-----------------------")
  selection=input("Please enter the letter of your selection. ")
  quantity=int(input("How many would you like? "))
  
  if selection.lower().strip()=="a":
    if pringles_Q > quantity:
      selection_made=True
      price=1
      total=price*quantity
      print("Your total is $", "{:.2f}".format(total), ". Please insert bills or coins.")
    else:
      print("Please check quantity available and make another selection.")
  elif selection.lower().strip()=="b":
    if pretzels_Q > quantity:
      selection_made=True
      price=.75
      total=price*quantity
      print("Your total is $", "{:.2f}".format(total), ". Please insert bills or coins.")
    else:
       print("Please check quantity available and make another selection.")
  elif selection.lower().strip()=="c":
    if sunchips_Q > quantity:
      selection_made=True
      price=.8
      total=price*quantity
      print("Your total is $", "{:.2f}".format(total), ". Please insert bills or coins.")
    else:
      print("Please check quantity available and make another selection.")
  elif selection.lower().strip()=="d":
    if cheetos_Q> quantity:
      selection_made=True
      price=.75
      total=price*quantity
      print("Your total is $", "{:.2f}".format(total), ". Please insert bills or coins.")
    else:
      print("Please check quantity available and  make another selection.")
  elif selection.lower().strip()=="e":
    if funyuns_Q>quantity:
      selection_made=True
      price=.75
      total=price*quantity
      print("Your total is $", "{:.2f}".format(total), ". Please insert bills or coins.")
    else:
      print("Please check quantity available and  make another selection.")
  elif selection.lower().strip()=="f":
    if doritos_Q> quantity:
      selection_made=True
      price=.75
      total=price*quantity
      print("Your total is $", "{:.2f}".format(total), ". Please insert bills or coins.")
    else:
      print("Please check quantity available and make another selection.")
  elif selection.lower().strip()=="g":
    if kitkat_Q>quantity:
      selection_made=True
      price=1.2
      total=price*quantity
      print("Your total is $", "{:.2f}".format(total), ". Please insert bills or coins.")
    else:
      print("Please check quantity available and make another selection.")
  elif selection.lower().strip()=="h":
    if reeses_Q>quantity:
      selection_made=True
      price=1.2
      total=price*quantity
      print("Your total is $", "{:.2f}".format(total), ". Please insert bills or coins.")
    else:
      print("Please check quantity available and  make another selection.")
  elif selection.lower().strip()=="i":
    if mandms_Q>quantity:
      selection_made=True
      price=1.2
      total=price*quantity
      print("Your total is $", "{:.2f}".format(total), ". Please insert bills or coins.")
    else: 
      print("Please check quantity available and  make another selection.")
  elif selection.lower().strip()=="j":
    if cookies_Q>quantity:
      selection_made=True
      price=1
      total=price*quantity
      print("Your total is $", "{:.2f}".format(total), ". Please insert bills or coins.")
    else:
      print("Please check quantity available and  make another selection.")
  else:
    print("Please make another selection.")
    
  
  if selection_made:
    currency=input("Please enter the letter to indicate the currency you will you be using. \n---BILLS:\nA. \t$20\nB. \t$10 \nC.\t$5 \nD. \t$1 \n---COINS: \nE. \t1.00 \nF.\t .50 \nG.\t .25 \nH.\t .10 \nI.\t .05 \nJ.\t .01\n")
    
    quant_currency=int(input("Enter quantity of this currency. "))
  
    payment(total,currency,quant_currency)
  print("--------------------------------")
  again=input("Would you like to make a purchase? Please enter \"Y\" for yes or \"N\" for no.")
  
  if again.lower().strip()=="y":
    place_order=True
  else:
    place_order=False