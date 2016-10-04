allGuests = {'Alice':{'apples':5,'pretzels':12},'Bob':{'ham sandwiches':3, 'apples':2}, 'Carol':{'cups':3, 'apple pies':1}}

def totalBrought(guests, food):
    numBrought = 0; #Initialize variable
    
    for k, v in guests.items(): #k is the name of the guests, picnic items is assigned to v, items() is a member function 
        numBrought += v.get(food,0) #food is the item that is passed through like apple that returns the value of apple
        print(k, v)
        print(v.get(food))
    return numBrought

print("Number of things being bought:")
print("-Apples      " + str(totalBrought(allGuests, 'apples')))