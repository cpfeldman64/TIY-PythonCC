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
cased_users = [x.lower() for x in current_users]

new_users = ['john', 'jane', 'lucy', 'lily', 'james']

for new_user in new_users:
    if new_user in current_users or cased_users:
        print("\nThis username is taken, please select another.")
    else:
        print("\nThat username is available!")

# still not working, come back to it later!