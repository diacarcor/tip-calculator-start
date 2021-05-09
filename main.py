print("Welcome to the tip calculator.")

#Ask for the bill amount
total_bill = float(input("What was the total bill? $"))

#Ask for the desire tip to pay as a float
tip = float (input("What percentage tip would you like to give? 10, 12, or 15? "))
#Convert the tip in a percentage
tip_percentage = tip / 100

#Ask for the number of people
people = int (input("How many people to split the bill? "))

#Add tip to the total bill
total_bill *=  (1+tip_percentage)

#Get the rounded value that each person should pay
each_person_value = "{:.2f}".format(total_bill / people,2)

#Create message to print
message = "Each person should pay: $" + each_person_value
#Print the result
print(message)


