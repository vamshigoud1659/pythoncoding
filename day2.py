

# a = int(input("enter a ="))
# b = int(input("enter b ="))
# sum = a+b
# if 10<=sum<=19:
#     print(20)
# else:
#     print(sum)

# a = int(input("enter a="))
# b = int(input("enter b="))
# c = int(input("enter c="))

# if a==13:
#   print(0)
# elif b==13:
#   print(a)
# elif c==13:
#   print(a+b)
# else:
#   print(a+b+c)


# a = int(input("enter a="))
# b = int(input("enter b="))
# c = int(input("enter c="))

# if a==b==c:
#   print(0)
# elif a==b:
#   print(c)
# elif b==c:
#   print(a)
# elif c==a:
#   print(b)
# else:
#   print(a+b+c)


speed = int(input("Enter speed= "))
birthday = int(input("enter 1 or 0: "))

if birthday:
    if speed<=65:
        print("no ticket")

    elif 65<=speed<=85:
        print("small ticket")

    else:
        print("big ticket")

else:
    if speed<=60:
        print("no ticket")
    
    elif 60<=speed<=80:
        print("small ticket")
   
    else:
        print("big ticket")
   
   



