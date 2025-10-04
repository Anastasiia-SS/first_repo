my_list = [1, 2, 3, 4, 5]
print(len(my_list))

nums = [3, 1, 4, 1, 5, 9, 2]
nums.sort(reverse=True)
print(nums)  # Виведе [1, 1, 2, 3, 4, 5, 9]

words = ["banana", "apple", "cherry"]
words.sort(key=len)
print(words)  # Виведе ['apple', 'banana', 'cherry']

my_dict = {"name": "Alice", "age": 25, "city": "New York"}
my_dict["age"] = 26  # Змінює вік на 26
my_dict["email"] = "alice@example.com"  # Додає нову пару ключ-значення
print(my_dict)


cat = {'nick': 'Simon', 'age': 7, 'characteristics': ['лагідний', 'кусається']}
info = {"status": "vaccinated", "breed": True}
cat.update({'status':  "vaccinated", "breed": True})
age = cat.get('age')
print(cat)

a = {1, 2, 3}
b = {3, 4, 5}
print(a.intersection(b))  # {3}
print(a & b)  # {3}

s = "Hello world!"
print(s[0])# H
print(s[-1])# !

name = 'John'
print('Hello, {}!'.format(name))

# Форматування з декількома аргументами
age = 25
print('Hello, {}. You are {} years old.'.format(name, age))

# Використання іменованих аргументів
print('Hello, {name}. You are {age} years old.'.format(name='Jane', age=30))

# Використання індексів для вказівки порядку аргументів
print('Hello, {1}. You are {0} years old.'.format(age, name))