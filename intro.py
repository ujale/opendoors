"""print('Hello World')
print(type(34.90))

article = "This is an article\na multiline article\n\t the period will be removed from this line.\b\n I want to see what this sequence does\r"
print(article)

"\nAnother example"
art = "Test\r carriage return.Test \vvertical tab. Then \\What about backslash"
print(art)

# Raw string
anotherArticle = r"This is an article,a multiline article\n\t the period will be removed from this line.\b\n "
print(anotherArticle)"""
"""result = 4
result += 3
print(result)
"""
"""age = 21
if age <= 10:
    print("You are too young")
elif age == 18:
    print("You can vote")
elif age == 12:
    print("You are now a teen")
#elif age != 12:
    #print("You are not 12 years")
elif age > 18:
    print('Oya na')
else:
    print("You are not too young")"""
"""number1 = 10
number2 = 20

if number1 == 10 and number2 == 20:
    print("\nNumber 1 is 10 and number2 is 20")

if number1 == 5 and number2 == 20:              # Will not be executed
    print("Number 1 may be 10 and number2 is 20")

if number1 == 5 or number2 == 20:
    print("\nNumber 1 may be 10 and number2 may be 20")

if not number1 == 10:               # Will not be executed since number1 is truly equal to 10
    print("NOT: Number 1 is 10")

if not number1 == 5:               # Will be executed since number1 is 5 which is not equal to 10
    print("\nNOT: Number 1 is not 10")"""

"""name = "python"
for character in name:
    print("character", character)
    
number = 5
for i in range(number):
    print("number", i)"""
"""number = 5
for i in range(number):
    if i == 3:
        break
    print("for: Number", i)
number = 5
while number > 0:
    if number == 3:
        break
    print("while: Number:", number)
    number -= 1"""
"""number = 10
for i in range(number):
    if i == 3:
        continue
    print("for: Number", i)
else:
    print("end of loop")
while number > 0:
    if number == 3:
        number -= 1
        continue
    print("while: Number:", number)
    number -= 1
else:
    print("end of loop")"""

def sum(num1=5, num2=3):
    print(num1 + num2)

sum()
sum(3)
sum(4,5)