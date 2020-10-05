stock={'Choclate cake':6,
'apple':0,
'Oranges':32,
'Apple Juice':15,}
prices={'Choclate cake': 4,
'apple':2,
'Oranges':1.5,
'Apple Juice':3}

def uppercase(x):
  return x[0].upper()+x[1:]

name=input('''What is your name?
''')
print('Hi, %s, welcome to my Infinity Cafe. Here is the menu:'%(name))
print()

def menu():
  for fruit in prices:
    print(uppercase(fruit))
    print('Price: $%s'%(prices[fruit]))
    print('Stock: %s'%(stock[fruit]))
    print()
  print('You have: $%s'%(money))
  print()

def ask_product(money):
  fruit=input('''What would you like to purchase?
''')
  print()
  if fruit in stock:
    if stock[fruit]>0:
      ask_amount(fruit,money)
    else:
      print('''Sorry, %ss are out of stock
'''%(fruit))
      ask_product(money)
  else:
    print('''Sorry, we don\'t have that, look at the menu.
    ''')
    ask_product(money)

def ask_amount(fruit,money):
  amount=int(input('''How many %ss do you want?
'''%(fruit)))
  print()
  if amount<=0:
    print('''At least buy one.
  ''')
    ask_amount(fruit,money)
  elif stock[fruit]>=amount:
    sell(fruit,amount,money)
  else:
    print('''Sorry, we don\'t have that many %ss.
    '''%(fruit))
    ask_amount(fruit,money)

def sell(fruit,amount,money):
  cost=prices[fruit]*amount
  confirmation=input('''Are you sure? That will be $%s.
-Yes
-No
'''%(cost)).lower()
  print()
  if confirmation=='yes':
    money-=cost
    print('''Thank you for the business!
''')
    stock[fruit]=stock[fruit]-amount
    ask_again()
  elif confirmation=='no':
    ask_product(money)
  else:
    print('''Answer me.
''')
    sell(fruit,amount,money)

def ask_again():
  answer=input('''Do you want anything else?
-Yes
-No
''').lower()
  print()
  if answer=='yes':
    menu()
    ask_product(money)
  elif answer=='no':
    print('Okay, bye.')
  else:
    print('Answer me.')
    ask_again()

money=117
menu()
ask_product(money)
