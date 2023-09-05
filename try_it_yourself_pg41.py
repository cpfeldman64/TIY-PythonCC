# Try it yourself Page 41

# Guest List

dinner_guests = [
    'ernest hemingway', 'michelle zauner', 'henry cavill'
]

print(f'\nThe guest list for dinner includes:\n{dinner_guests}.\n')

eh_message = f'{dinner_guests[0].title()}, I would be delighted to have you at my dinner table!\n'

mz_message = f'\n{dinner_guests[1].title()}, please enjoy a nice meal with us!\n'

hc_message = f'\n{dinner_guests[-1].title()}, thank you for attending this evening!\n'

print(eh_message + mz_message + hc_message)


# Guest List Adjustments

not_attending = dinner_guests[0]

dinner_guests_pop = dinner_guests.pop(0)

print(f"{not_attending.title()} wont't be able to make it.\n")

dinner_guests.insert(0, 'john green')

jg_message = f'Instead, {dinner_guests[0].title()}, please join us this evening!\n'

print(jg_message)
print(f'The new guest list will include:\n{dinner_guests}.\n')

# We found a bigger table!

bigger_table = 'we found a bigger table!'
new_guests = [
    'timothee chalamet','cillian murphy', 
    'brandon sanderson','chris hemsworth',
]

tc_message = f'{new_guests[0].title()}, {bigger_table} Please join us.\n'
cm_message = f'{new_guests[1].title()}, {bigger_table} Please join us.\n'
bs_message = f'{new_guests[2].title()}, {bigger_table} Please join us.\n'
ch_message = f'{new_guests[3].title()}, {bigger_table} Please join us.\n'

print(f'{tc_message}{cm_message}{bs_message}{ch_message}')

dinner_guests.append(new_guests[0])
dinner_guests.insert(3, new_guests[1])
dinner_guests.insert(0, new_guests[2])
dinner_guests.insert(-1, new_guests[-1])


print(f'The new guest list will include:\n{dinner_guests}.\n')

print(f'{len(dinner_guests)} is the number of guests in attendance.\n')

# Table not ready! Pop()

print(
    'Oh no! Our table is not ready. We only have room for two guests. Sorry!'
)

guest_pop1 = dinner_guests.pop()
print(f'\n{guest_pop1.title()}, so sorry to cancel on you.')

guest_pop2 = dinner_guests.pop()
print(f'\n{guest_pop2.title()}, so sorry to cancel on you.')

guest_pop3 = dinner_guests.pop()
print(f'\n{guest_pop3.title()}, so sorry to cancel on you.')

guest_pop4 = dinner_guests.pop()
print(f'\n{guest_pop4.title()}, so sorry to cancel on you.')

guest_pop5 = dinner_guests.pop()
print(f'\n{guest_pop5.title()}, so sorry to cancel on you.')

print(f'\nThe new guest list will include:\n{dinner_guests}.\n')


#Empty the list!

dinner_over = ('Dinner is now over!')
thank_you = f' {dinner_guests[0].title()}, {dinner_guests[1].title()}, thank you for coming!'
print(dinner_over + thank_you)
dinner_guests.remove('john green')
dinner_guests.remove('brandon sanderson')

print(f'\n{len(dinner_guests)} is the number of guests left at the restaurant.')

