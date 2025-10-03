print("Hello world")

print("Hello git")

age = 32
print(age)

name = "Anastasiia"
print(name)

age = "banana"
print(age)

rate = 1.68
value = 326
payment = rate * value
print(payment)

rate = 1.68
rate_night = rate / 2
value_day = 221
value_night = 196
payment = rate * value_day + rate_night * value_night
print(payment)

first_name = "Anastasiia"
last_name = "Siryk"
full_name = first_name + " " + last_name
print(full_name)

length = 2.75
width = 1.75
area = length * width
show = f"With width {width}m and length {length}m of the area is {area}m2"
print(show)

length = "2.75"
width = "1.75"
area = float(length) * float(width)
show = f"With width {width}m and length {length}m of the area is {area}m2"
print(show)

name = input("What is your name? ")
email = input("what is your email? ")
age = int(input("what is your age? "))
heught = float(input("What is your height? "))
is_active_input = input("Бажаєте отримувати повідомлення від сайту? (так або просто натисніть Enter для відмови): ").strip().lower()
is_active = True if is_active_input == "так" else False
