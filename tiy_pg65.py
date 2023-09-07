# Try it yourself page 65

# Slices

cats = ['calico', 'tabby', 'black', 'white', 'ginger']

print("\nThe first three items in the list are:")
print(cats[:3])

print("\nThree items from the middle of the list are:")
print(cats[1:4])

print("\nThe last three items in the list are:")
print(cats[-3:])

# My Pizzas, Your Pizzas

pizzas = [ 'supreme', 'pepperoni', 'mushroom']
friend_pizzas = pizzas[:]

pizzas.append('hawaiian')

print("\nMy favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)

# Prints each pizza in the pizzas list one time

