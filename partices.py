# plant=str(input("Enter a spathiphyllum plant (upper or lower case):"))
# if plant=="Spathiphyllum":
#     print("Yes , Spathiphyllum is a best plant ever !")
# elif plant=="spathiphyllum":
#     print("No, I want big spathiphyllum")
# else:
#     print("Spathiphyllum is Not! found")


    
#Q2

# income=float(input("entre a annual income (in thalers):"))
# if income==0:
#     tax=0.0       
# elif income<=85528:
#     tax=(0.18*income)-556.02
 
# elif income>85528:
#     surplus=income-85528
#     tax=14839.02+(0.32*surplus)    

# tax=round(tax)    

# print("the calculated tax is = ",tax)

# 03

laep_year = int(input("Enter a year :"))
if laep_year%4==0:
    print("the year is leap year ")
elif laep_year%100==0 :
    print("the year is leap year.")
elif laep_year%400==0:
    print("the is common year.")    
else:
    print("the year is commom year. ")
    
