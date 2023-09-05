# Try it yourself page 45

places = [
    'germany', 'france', 'japan', 'italy', 'greece'
]

print(places)

sorted_places = sorted(places)
print(f'\n{sorted_places}')

print(f'\n{places}')

print(f'\n{sorted(places, reverse=True)}')

print(f'\n{places}')

places.reverse()
print(f'\n{places}')

places.reverse()
print(f'\n{places}')

places.sort()
print(f'\n{places}')

places.sort(reverse=True)
print(f'\n{places}')




# Every Function

dogs = [
    'husky', 'golden retriever', 'corgi', 'doberman', 'dalmatian'
]
print(f'\n\n{dogs}\n')
dogs.sort()
print(dogs)
message = f'\nMy favorite dog is a {dogs[3].title()}.'
print(message)

pop_dog1 = dogs.pop()
pop_dog2 = dogs.pop()
dogs.insert(0, 'golden retriever')
dogs.append('husky')

print(f"\nI've put {dogs[0].title()} at the front of the list.\n")
print(dogs)
