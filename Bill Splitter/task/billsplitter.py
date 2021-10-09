import random


print('Enter the number of friends joining (including you):')
count = int(input())
if count < 1:
    print('No one is joining for the party')
    exit()

print('Enter the name of every friend (including you), each on a new line:')
friend_list = [input() for _ in range(count)]

print('Enter the total bill value:')
total_bill = int(input())
split_amount = round(total_bill / count, 2)
split_bills = dict.fromkeys(friend_list, split_amount)

print('Do you want to use the "Who is lucky?" feature? Write Yes/No')
confirm = input()
if confirm == 'Yes':
    lucky_one = random.choice(list(split_bills.keys()))
    print(f"{lucky_one} is the lucky one!")
    split_amount = round(total_bill / (count - 1), 2)
    split_bills = dict.fromkeys(friend_list, split_amount)
    split_bills[lucky_one] = 0
else:
    print('No one is going to be lucky')

print(split_bills)
