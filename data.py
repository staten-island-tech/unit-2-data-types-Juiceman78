""" #Strings are for representing characters, names, words etc.
name ="Deivid"
#integer represents whole numbers
age: 14
#Floats represents decimals
wallets = 5.45
#boolean represents true or false, used in evaluations
graduated = False

def add(x,y): 
    print(x + y)
#input asks the user a question and stores their response as a value
bill=float(input("what was the bill"))
print*(type(bill))
add(40,bill)

#lists
students = ["Joanna", "Deivid", "David", "other David", "Ethan"]
#similar to saying for i in range(5) print(students[i])
print(students[4])
for student in students:
    print(student)
moneys = [1,2,3,4,5,6]
total = 0
for money in moneys:
    total = total + money
    print(total)
 """

""" x = 3
y = float(3)
print(x,y) """

""" values = [1,2.23,5,7,2,30,15]
print(values)
for i in values:
    print(i) """

""" "test"
["t","e","s","t"] """

""" x = "this is a thing"
y= x.split( )
z = y[0]
print(y)
print(z) """

""" def sentence():
    answer = input("Type your sentence here: ")
    words = answer.split()  
    sigma = len(words)  
    print(sigma)  
    for word in words:  
        print(word) 
sentence() """

""" def madlib():
    verb1 = input("Type a Verb: (Example:Gooned,Mogged,Simped)")
    verb2 = input("Type a Verb: (Example:Smash,Cap,Ghost)")
    noun = input("Type a Noun: (Example:Sigma,BabyGronk,SkibidiToilet) ")
    number = input("Type a Number: (Example: 6,9,23)")
    celebs = input("Type a Celebrity: (Example:LebronJames,BigJustice,FrankOcean)")

    madlib_story = f"One day {celebs} decided to go to a certain party. They found a красивый {noun} that gave them {number} big booms. As fast as {celebs} could they {verb1} all around the world. But suddenly {noun} decided to {verb2} right into {celebs}. What a way to show {celebs}'s love! "

    print(madlib_story)
madlib() """

""" x = "test"
print(f"hello {x}")

temp = 75
if temp > 68:
    print('warm')
elif temp == 68:
    print('perfect')
else:
    print('cold') """

""" def oddeven(number):
    if number % 2 == 0:
        print("even")
    else:
        print("odd")

number = int(input("Enter a number: "))
oddeven(number)
 """

""" def tip():
    bill = input("How was the service? Bad, Okay, Good, Or Great")
    if bill == "Bad":
        tip = "0%"
    elif bill == "Okay":
        tip = "15%"
    elif bill == "Good":
        tip = "20%"
    elif bill == "Great":
        tip = "25%"

    print(f"Suggested tip: {tip}")
tip() """

""" def find_factors():
    factors = []
    n = int(input("Please enter a number: "))
    for i in range(1, n + 1):  
        if n % i == 0:  
            factors.append(i)  
    return factors

print(find_factors()) """

""" def find_gcf():
    gcf = [] #Defines the variables (PS. Whalen dont nuke my HOS all these notes are for my reference =) 
    number1 = int(input("Please enter the 1st number: ")) #Creates an input and converts into an integer
    number2 = int(input("Please enter the 2nd number: "))


    for i in range(1, min(number1, number2) + 1):  # Defines the range from 1 to the lowest
        if number1 % i == 0 and number2 % i == 0: #Creates an if condition which finds the number that has a remainder of 0 in these lists
            gcf.append(i)  #Adds these numbers into the list of Gcf

   
    greatest_common_factor = max(gcf) if gcf else None #defines the variable as the GCF by using the max command; and if there isn't a number it says there is a none 

   
    print(f"The greatest common factor (GCF) of {number1} and {number2} is: {greatest_common_factor}") #Prints the GCF of the 2 numbers


find_gcf() """


        
            