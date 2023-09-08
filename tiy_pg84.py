# Try it yourself page 84

# Alien Colors 1:

alien_color = 'red'
if alien_color == 'green':
    print("5 points!")

new_alien_color = 'green'
if new_alien_color == 'green':
    print("5 points!")

# Alien Colors 2:

alien_color_2 = 'blue'
if alien_color_2 == 'green':
    print("5 points!")
else: 
    print("10 points!")

alien_color_3 = 'green'
if alien_color_3 == 'green':
    print("5 points!")
else: 
    print("10 points!")

# Alien colors 3:

alien_color_4 = 'red'
if alien_color_4 == 'green':
    print("5 points!")
elif alien_color_4 == 'yellow':
    print("10 points!")
elif alien_color_4 == 'red':
    print("15 points!")
else:
    print("20 points!")

alien_color_5 = 'green'
if alien_color_5 == 'green':
    print("5 points!")
elif alien_color_5 == 'yellow':
    print("10 points!")
elif alien_color_5 == 'red':
    print("15 points!")
else:
    print("20 points!")

alien_color_6 = 'yellow'
if alien_color_6 == 'green':
    print("5 points!")
elif alien_color_6 == 'yellow':
    print("10 points!")
elif alien_color_6 == 'red':
    print("15 points!")
else:
    print("20 points!")

alien_color_7 = 'orange'
if alien_color_7 == 'green':
    print("5 points!")
elif alien_color_7 == 'yellow':
    print("10 points!")
elif alien_color_7 == 'red':
    print("15 points!")
else:
    print("20 points!")


# Stages of life

age = 23
if age <= 2:
    print("Baby!")
elif (age > 2) and (age < 4):
    print("Toddler!")
elif (age > 4) and (age < 13):
    print("Kid!")
elif (age > 13) and (age < 20):
    print("Teenager!")
elif (age > 20) and (age < 65):
    print("Adult!")
elif (age > 65):
    print("Elder!")

# Favorite Fruits

favorite_fruits = [
    'peaches', 'watermelon', 'cherries', 'mango', 'strawberries'
]

if 'peaches' in favorite_fruits:
    print('Peaches are good!')
if 'blueberries' in favorite_fruits:
    print('Blueberries are good!')
if 'watermelon' in favorite_fruits:
    print('Watermelon is good!')
if 'bananas' not in favorite_fruits:
    print("Bananas aren't my favorite!")
