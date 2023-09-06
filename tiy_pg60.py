# Try it yourself page 60

# Counting to Twenty:

#for value in range(1,21):
    #print(value)

# One Million
#for value in range(1,1_000_001):
    #print(value)

# Summing a Million
million_list = list(range(1,1_000_001))
#print(f'\n{million_list}')
print(f'\n{min(million_list)}')
print(f'\n{max(million_list)}')
print(f'\n{sum(million_list)}')

# Odd Numbers
odd_numbers = list(range(1, 21, 3))
for value in odd_numbers:
    print(value)

# Threes
thirds = [value*3 for value in range(1,11)]
print(f'\n{thirds}\n')
# whoo!

# Cubes
cubes = [value**3 for value in range(1,11)]
print(f'\n{cubes}\n')

cube_values = []
for value in range(1,11):
    cube = value**3
    cube_values.append(cube)
print(cube_values)