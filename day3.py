# day = int(input("enter day:"))
# on_vacation = int(input("enter 0 or 1:"))

# if on_vacation:
#     if 1<=day<=5:
#        print("10:00AM")
#     else:
#        print("OFF")

# else:
#     if 1<=day<=5:
#        print("7:00AM")
#     else:
#         print("10:00AM")

# small = int(input("enter small brick:"))
# big = int(input("enter big brick:"))
# goal = int(input("enter goal:"))

# if goal >= big*5:
#     remaining = goal - big*5
# else:
#     remaining = goal%5 

# if small>=remaining:
#     print(True)
# else:
#     print(False)

a = int(input("enter a:"))
b = int(input("enter b:"))
c = int(input("enter c:"))

if abs(a-b) <=1:
    if abs(a-c)>=2 and abs(b-c)>=2:
        print(True)
    else: 
        print(False)
elif abs(a-c) <=1:
    if abs(a-b)>=2 and abs(c-b)>=2:
        print(True)
    else:
        print(False)
else:
     print(False)

    