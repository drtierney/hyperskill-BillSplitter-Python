# write your code here
print('Enter the number of friends joining (including you):')
count = int(input())
if count < 1:
    print('No one is joining for the party')
    exit()

print('Enter the name of every friend (including you), each on a new line:')
friends = [input() for _ in range(count)]

print("Enter the total bill value:")
total_bill = int(input())
split_amount = round(total_bill / len(friends), 2)
friends_bills = dict.fromkeys(friends, split_amount)
print(friends_bills)
