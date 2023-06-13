# Yanet Rodriguez

# June 11, 2023

#Lab 9 Problems

print("")


# Problem 1-Infinite loop is located after problem # 4


print("")

#Problem 2-Appends to list at every iteration
L = []
counter = 0

while counter <= 10:
    L.append(counter) # adds new value of counter to the list
    counter = counter + 1
    print (L)


print("")
# Problem 3-Adds inputs from user to list
L = []

while (sum(L)) <= 100:
    number = int(input("Enter Number: ")) # user enters number to be added to list
    L.append(number) #adds number entered by user to the list L

print ("The sum is ", sum(L))

print("")

# Problem 4 - loops until counter reaches
tens = []
counter: int = 0

while counter <= 50:
    if counter % 10 == 0:
        tens.append(counter)
    counter = counter + 1

print (tens)

print("")

# Problem 1-Infinite loop
n = 1
while n < 5: #Creates an infinite loop 1 will always be less than 5
    print ("Infinite")