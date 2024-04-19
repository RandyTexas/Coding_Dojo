num1 = 42 # variable declaration
num2 = 2.3 # variable declaration
boolean = True # variable declaration
string = 'Hello World' # variable declaration
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # variable declaration
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # variable declaration
fruit = ('blueberry', 'strawberry', 'banana') # variable declaration
print(type(fruit)) # - tuple

print(pizza_toppings[1]) # - Sausage

pizza_toppings.append('Mushrooms')
print(person['name']) # John 

person['name'] = 'George'
person['eye_color'] = 'blue'

print(fruit[2]) # - banana

if num1 > 45:
    print("It's greater") # Boolean
else:
    print("It's lower") # Boolean The else statement is executed because num1 is not greater than 45

if len(string) < 5:
    print("It's a short word!") # This would not run becuase the string is longer than 5
elif len(string) > 15:
    print("It's a long word!") # This would not run because the string is not longer than 15
else:
    print("Just right!") # This would show 

for x in range(5):
    print(x) # 0,1,2,3,4
for x in range(2,5):
    print(x) # 2,3,4
for x in range(2,10,3):
    print(x) # 2,5,8
x = 0
while(x < 5):
    print(x) # 0,1,2,3,4
    x += 1

pizza_toppings.pop()
pizza_toppings.pop(1)

print(person) # George, Salt Lake, 37, False, blue
person.pop('eye_color')
print(person) # George, Salt Lake, 37, False

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement') # it would print this 3 times because we poped 2 items from the list the last one and index of 1
    if topping == 'Olives':
        break

def print_hello_ten_times():
    for num in range(10):
        print('Hello') #  hello will print 10 times

print_hello_ten_times()

def print_hello_x_times(x):
    for num in range(x):
        print('Hello') # hello will print 4 times

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello') # hello will print 10 times then print 4 times

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)