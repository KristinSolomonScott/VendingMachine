'''Vending Machine
IU Summer 2022
Kristin Scott'''

import random

#################################################
'''
change_total is a parameter used by the return_change function. It holds the amount of change owed to a customer after currency has been inserted following a purchase

change_msg is a local string variable used in the return_change function. It prints a description of the currency returned to a customer.

amt_to_return is a local numeric variable used in the return_change function. It starts as the total of the amount that needs to be returned to the customer and changes as currency is returned until it equals 0. 

owed is a parameter used by the payment function. 

cur is a parameter used by the payment function.

quant is a parameter used by the payment function.

pmnt is a local numeric variable used in the payment function.

still_owed is a local numeric variable used in the payment function.

The following variables (each followed by _Q) hold the quantity of the variable named:
pringles_Q 
pretzels_Q
sunchips_Q
cheetos_Q
funyuns_Q
doritos_Q
kitkat_Q
reeses_Q
mandms_Q
cookies_Q

place_order is a booelan variable used with a while loop to see if customer would like to continue to buy snacks

selection_made is a boolean variable used to keep track of whether or not the user has selected an item for purchase. It is set to True if the number of items available is at least as high as the number the user would like to purchase

selection is a string the user enters to indicate their choice of items

quantity is a numeric variable used to indication the number of items the user would like to purchase


price is a numeric variable and its value is set depending on which item was chosen

total is a numeric variable that holds the value of price*quantity

currency is a string variable used to indicate the value of the currency the user has entered

quant_currency is a numeric variable used to indicate the number of a particular currency that has been entered

again is a boolean variable used when asking if the customer would like to make another purchase 

'''
#################################################

#takes the amount of changed owed to customer and returns a string describing the change being returned
def return_change(change_total):
  change_msg="Your change is: \n"
  amt_to_return=change_total

  while int(amt_to_return) >= 20:
    amt_to_return -=20
    change_msg = change_msg + "a twenty dollar bill\n"
  while int(amt_to_return) >= 10:
    amt_to_return -=10
    change_msg = change_msg + "a ten dollar bill\n"
  while int(amt_to_return) >= 5:
    amt_to_return -=5
    change_msg = change_msg + "a five dollar bill\n" 
  while int(amt_to_return) >= 1:
    amt_to_return -=1
    change_msg = change_msg + "a one dollar bill\n"
  while amt_to_return >= .5:
    amt_to_return -=.5
    change_msg = change_msg + "one fifty cent coin\n"
  while amt_to_return >= .25:
    amt_to_return -=.25
    change_msg = change_msg + "a quarter\n"
  while amt_to_return >= .1:
    amt_to_return -=.1
    change_msg = change_msg + "a dime\n"
  while amt_to_return >= .05:
    amt_to_return -=.05
    change_msg = change_msg + "a nickel\n"
  while amt_to_return >= .01:
    change_msg = change_msg + "a penny\n"
    amt_to_return -=.01


  

  
  print(change_msg)
  

#takes the amount owed, the currency entered, and the quantity of the currency entered...returns a message informing customer how much is still owed & allows them to continue entering currency until amount owed is reached. When amount owed has been reached, prints a message telling customer to pick up item. 
def payment(owed,cur,quant):
  pmnt=0
  still_owed=owed
  
  if cur.upper().strip()=="A":
      pmnt=20*quant
  elif cur.upper().strip()=="B":
      pmnt=10*quant
  elif cur.upper().strip()=="C":
      pmnt=5*quant
  elif cur.upper().strip()=="D" or cur.upper().strip()=="E":
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

  still_owed=still_owed-pmnt

  
  if still_owed==0:
    print("Please pick up your snack below. Have a nice day!")
    
    
  elif still_owed > 0:  
      print("Amount due=", "{:.2f}".format(still_owed))
      print("--------------------------")
      currency=input("Please enter the letter to indicate the currency you will you be using. \nBILLS:\nA. \t$20\nB. \t$10 \nC.\t$5 \nD. \t$1 \nCOINS: \nE. \t1.00 \nF.\t.50 \nG.\t.25 \nH.\t.10 \nI.\t.05 \nJ.\t.01\n")
  
      quant_currency=int(input("Enter quantity of this currency. \n"))

      payment(still_owed,currency,quant_currency)
    
  elif still_owed < 0:
      still_owed= 0-still_owed
      return_change(still_owed)
      #print("Your change is ", ("{:.2f}".format(still_owed)))
      print("Please take your change and pick up your snack below. Have a nice day!")
      still_owed=0
      









#declaring variables for items in machine

pringles_Q=random.randrange(10) #a

pretzels_Q=random.randrange(10) #b

sunchips_Q=random.randrange(10) #c

cheetos_Q=random.randrange(10) #d

funyuns_Q=random.randrange(10)   #e

doritos_Q=random.randrange(10)  #f

kitkat_Q=random.randrange(10)  #g

reeses_Q=random.randrange(10)   #h

mandms_Q=random.randrange(10)    #i

cookies_Q=random.randrange(10)    #j





place_order=True #variable used to see if customer would like to make another order
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
    if pringles_Q >= quantity:
      selection_made=True
      price=1
      total=price*quantity
      print("Your total is $", "{:.2f}".format(total), ". Please insert bills or coins.")
    else:
      print("Please check quantity available and make another selection.")
  elif selection.lower().strip()=="b":
    if pretzels_Q >= quantity:
      selection_made=True
      price=.75
      total=price*quantity
      print("Your total is $", "{:.2f}".format(total), ". Please insert bills or coins.")
    else:
       print("Please check quantity available and make another selection.")
  elif selection.lower().strip()=="c":
    if sunchips_Q >= quantity:
      selection_made=True
      price=.8
      total=price*quantity
      print("Your total is $", "{:.2f}".format(total), ". Please insert bills or coins.")
    else:
      print("Please check quantity available and make another selection.")
  elif selection.lower().strip()=="d":
    if cheetos_Q>= quantity:
      selection_made=True
      price=.75
      total=price*quantity
      print("Your total is $", "{:.2f}".format(total), ". Please insert bills or coins.")
    else:
      print("Please check quantity available and  make another selection.")
  elif selection.lower().strip()=="e":
    if funyuns_Q>= quantity:
      selection_made=True
      price=.75
      total=price*quantity
      print("Your total is $", "{:.2f}".format(total), ". Please insert bills or coins.")
    else:
      print("Please check quantity available and  make another selection.")
  elif selection.lower().strip()=="f":
    if doritos_Q>= quantity:
      selection_made=True
      price=.75
      total=price*quantity
      print("Your total is $", "{:.2f}".format(total), ". Please insert bills or coins.")
    else:
      print("Please check quantity available and make another selection.")
  elif selection.lower().strip()=="g":
    if kitkat_Q>= quantity:
      selection_made=True
      price=1.2
      total=price*quantity
      print("Your total is $", "{:.2f}".format(total), ". Please insert bills or coins.")
    else:
      print("Please check quantity available and make another selection.")
  elif selection.lower().strip()=="h":
    if reeses_Q>= quantity:
      selection_made=True
      price=1.2
      total=price*quantity
      print("Your total is $", "{:.2f}".format(total), ". Please insert bills or coins.")
    else:
      print("Please check quantity available and  make another selection.")
  elif selection.lower().strip()=="i":
    if mandms_Q>= quantity:
      selection_made=True
      price=1.2
      total=price*quantity
      print("Your total is $", "{:.2f}".format(total), ". Please insert bills or coins.")
    else: 
      print("Please check quantity available and  make another selection.")
  elif selection.lower().strip()=="j":
    if cookies_Q>= quantity:
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

#check to see if customer would like to place another order
  
  again=input("Would you like to make a purchase? Please enter \"Y\" for yes or \"N\" for no.")
  
  if again.lower().strip()=="y":
    place_order=True
  else:
    place_order=False
