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

def sentence(input):
    print("Type your sentence here")
    sigma = sentence.split()