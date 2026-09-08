age=int(input("enter num="))

if age>=18:
    license=input("Do you have license:")
    if license=='yes':
         print("Eligible for driving")
    else:
        print("GET YOUR LICENSE")
else:
    print("NOT eligible for driving")
    