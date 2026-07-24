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

# laep_year = int(input("Enter a year :"))
# if laep_year%4==0:
#     print("the year is leap year ")
# elif laep_year%100==0 :
#     print("the year is leap year.")
# elif laep_year%400==0:
#     print("the is common year.")    
# else:
#     print("the year is commom year. ")

#04


# beatles=[]
# beatles.append("john lennon")
# beatles.append("paul Mccartney")
# beatles.append("george harrsion")
# i=0

# for i in beatles:
#     if (beatles.count == 3):
#         beatles.append("stu sutcliffe")
#     else:
#         beatles.append("pete best")
# print(beatles)   

# # for i in range(2): 
# #     if i==0:
# #         beatles.append("stu sutcliffe")
# #     else:
# #         beatles.append("pete best")
        
# del beatles[-1]
# del beatles[-1]
# beatles.insert(0,"ringo starr")

# print(beatles)


# num=int(input("enter a number :"))
# # for j in range (1,11):
# #     print(f'{num}*{j}={num*j}')

# lst=[2,2,2,3,4,2,6,4,4,5,9]
# new_list=[]
# for index in lst:
#     if index not in new_list:
#         new_list.append(index)
        
    
# print(new_list)   


my_list=[3,11,5,17,1,9,7,15,13]
# largest_number=0

# for i in my_list:
#     if i>largest_number:
#         largest_number=i
# print("the largest no. is:",largest_number)        


my_list.sort()
print("the largest number is=",my_list[8])
