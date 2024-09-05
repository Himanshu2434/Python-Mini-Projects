#Rent Calculator 
#Author: [Himanshu]

#Enter flat or hostel rent
rent = int(input("Enter the Rent of Flat/Hostel :"))

#Enter the cost of grocery
food=int(input("Enter the Cost of Food/Grocery :"))

#Enter the no of electricity used
electricity=int(input("Enter the Amount of Electricity Used :"))

#Enter the cost of 1 unit 
electrictiy_cost = int(input("Enter the Per Unit Cost of electricity :"))

#Enter the cost of internet or wifi broadband
internet= int(input("Enter the Cost of Internet/Wifi :"))

# Enter the No of peoples
people = int(input("Enter the No. of People Living :"))

#Total amount 
total= rent+food+(electricity * electrictiy_cost )+internet

# Total amount divided by number of peoples 
per_person = total / people

#Final Output amount to pay per person
print("Total Expenses per Person is : ",per_person)