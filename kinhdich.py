import random


list , list1 = [] , []

for i in range(1,7):
    num = 0
    for j in range(1,4):
        coin = random.choice(["heads", "tails"])
        if coin == "heads":
            num += 1
    if num == 0:
        list.append(2)
        list1.append(1)
    elif num == 3:
        list.append(1)
        list1.append(2)
    else:
        list.append(num)
        list1.append(num)
        
print(list)
print(list1)



    
    