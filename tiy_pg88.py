# Try it yourself page 88

# Hello Admin & No Users
# 'admin', 'honkeytonk', 'crusher', 'yankeedoodle', 'louis'
usernames = ['admin', 'honkeytonk', 'crusher', 'yankeedoodle', 'louis']
if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello admin!")
        elif username == 'honkeytonk':
            print("Hello honkeytonk!")
        elif username == 'crusher':
            print("Hello crusher!")
        elif username == 'yankeedoodle':
            print("Hello yankeedoodle!")
        elif username == 'louis':
            print("Hello louis!")
else:
    print("We need to find some users!")

# This loop will print the appropriate message if list is empty.

# Checking Usernames
current_users = ['James', 'Lily', 'Harry', 'Hermione', 'Ron']
current_users_lower = ['james', 'lily', 'harry', 'hermione', 'ron']
new_users = ['Joseph', 'Lauren', 'james', 'Lily']

for new_user in new_users:
    if new_user  in current_users:
        print("\nThis username is taken, please select another.")
    elif new_user in current_users_lower:
        print("\nThis username is taken, please select another.")
    else:
        print("\nThat username is available!")

print('\n\n\n')

# I've made it case insensitive, but I want to know how I can convert the whole
# list to lowercase and store that as a variable.

# In theory this could still work so long as when a new user is added they
# are simulatenously populated to the current_users and current_users_lower
# list. Still weird though. I feel like it could be cleaner but idk how.


# Ordinal Numbers

numbers = list(range(1,10))
for number in numbers:
    if number == 1:
        print(f'{number}st!')
    elif number == 2:
        print(f'{number}nd!')
    elif number == 3:
        print(f'{number}rd!')
    else:
        print(f'{number}th!')

# whoo!


