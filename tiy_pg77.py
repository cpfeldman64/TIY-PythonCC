# Conditional Tests

cat = 'calico'
print("Is cat == 'calico'? I predict True.")
print(cat == 'calico')

print("\nIs cat = 'tabby'? I predict False.")
print(cat == 'tabby')


dog = 'golden retriever'
print("\nIs dog = 'golden retriever'? I predict True.")
print(dog == 'golden retriever')

print("\nIs dog = 'golden retriever'? I predict False.")
print(dog == 'husky')

# More conditional tests

true_string = 'What is a dog'
print(f'\nIs the question:\n\t{true_string}?\nI predict true.')
print(f'\n{true_string == "What is a dog"}')
# good to know that you can put boolean expressions inside of f-strings

name = 'connor'.lower()
print(f"\nIs your name 'Connor'?")
print(name == 'Connor')
# boolean shows this as false because the variable is specified to be
# all lowercase, and the question is asking if it is titlecase

# Numerical Conditional Tests

correct_number = 12
print("\nIs the number greater than 10? I predict true.")
print(correct_number >= 10)
print("\nIs the number less than 10? I predict false.")
print(correct_number <= 10)
print("\nIs the number 12?")
print(correct_number == 12)

# Conditionals using AND and OR

number_1 = 5
number_2 = 15
print("\nAre these number less than 20?")
print((number_1 <= 20) and (number_2 <= 20))
print("\nAre either of these numbers single digit?")
print((number_1 <= 10) or (number_2 <= 10))


# Testing whether an item is in a list

dogs = ['husky', 'poodle', 'corgi', 'golden']
print("\nAre huskies one of you favorite dogs?")
print('husky' in dogs)
print("\nAre bulldogs one of your favorite dogs?")
print('bulldog' in dogs)


