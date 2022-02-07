
hight = int(input("wht is your hight?"))
bill =  0 

if hight >= 120:
    print("you can ride ")
    age = int(input("wht is your age ?"))
    if age<=12:
        bill = 5
        print("child tickets are  $5")
    elif age <= 18:
        bill = 7
        print("youth  tickets are  $7")
    elif age>=18 and 45<=age<=55:
        print("your ride is free!!")

    else:
        bill = 12 
        print("adult tickets are  $12")
    
    photo = input("Do you want to have a photo? y or n")
    if photo == "y":
        bill += 3 
    print(f"Your bill is {bill}")
    # if age >=18 and 45<=age<=55:
    #     bill = 0 
    #     print(f"your bill is {bill}")


else: 
    print("you can not ride ")