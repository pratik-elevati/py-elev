
name = "patrick"   #string
age = 22           #integer
height = 5.6       #float
is_intern = True   #boolean

# to convert data types
age_str = str(age)     # integer to string      
age_float = float(age) # integer to float
str(height)            # float to string

current_year = 2025
birth_year = current_year - age
print(birth_year)

user_name=input("Enter your name: ")
age = int(input("Enter your age: "))

print("hey " + user_name + " , youre " + str(age) + " years old")

age += 20
print("new age = " ,age)

# if else loops

people = 6

if people <= 2:
    print("bike")
elif people == 3:
    print("auto")
elif 3 < people <= 5:
    print("car")
else:
    print("bus") 

# loops

for i in range(10):
    print(f"number: {i}")

cars = ['bmw', 'audi', 'toyota', 'subaru']
for car in cars:
    if car == 'bmw':
        print(car)
    else:
        print("not bmw")    

countdown = 10
while countdown > 0:
    print(countdown)
    countdown -= 1 
print("Lift off")

name = True
while name:
    user_input = input("Type 'exit' to stop: ")
    if user_input.lower() == 'exit':
        name = False    
        print("Loop ended.")
# break statement

while True:
    attempt = input("enter password: ")
    if attempt == "hi":
        print("access granted")
        break  
    else:
        print("access denied")
        
while True:
    attempt = input("Enter the password: ")

    if attempt == "test111":
        print("Access granted")
        break
    else:
        print("Wrong password, try again.")


# Function Definition
def calculate_area(length, width):
    area = length * width
    return area

# Function Call 
room_area = calculate_area(length=5, width=12)
print(f"The room area is: {room_area} square units.")


