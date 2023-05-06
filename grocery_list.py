grocery_item = [] #create/define an empty list of grocery items

grocery_history = []

#Variable used to check if the while loop condition is met
stop = 'go'

while stop == 'go' or stop == 'c': #using a while loop, user is prompted to input data until they no longer have an any items to enter 
  item_name = input("Item name:\n")
  quantity = input("Quantity purchased:\n")
  cost = input("Price per item:\n")
  
  grocery_item = {'name':item_name, 'number': int(quantity), 'price': float(cost)} #creates a dictionary of grocery items based on user input
  grocery_history.append(grocery_item) #creates a list of dictionaries of items based on the number of items the user inputs
  stop = input("Would you like to enter another item?\nType 'c' for continue or 'q' to quit:\n")


grand_total = 0
for item in grocery_history: #loops through a list of dictionaries based on the specific items in the list created/modified above until all the items are looped through
  item_total = item['number'] * item['price'] #accesses the value of the keys, number & price, in the dictionary of each iterated list that results into a new value: item_total
  grand_total = grand_total + item_total
  print(str(item['number']) + ' '+ item['name'] + ' @ $%.2f' % item['price'] + ' ea $%.2f' % item_total)
  item_total = 0
print('Grand total: $%.2f' % grand_total)