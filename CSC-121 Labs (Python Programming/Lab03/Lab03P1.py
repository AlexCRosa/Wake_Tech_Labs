#
# Alex Cesar Rosa
# 1/22/2024
# Inventory Estimator
#

# Get the starting numbers of paperbacks and hardbacks.
books = int(input('What is the current number of books? '))
dvds = int(input('What is the current number of DVDs? '))
games = int(input('What is the current number of games? '))
print()

# Display the inventory stock table.
for month in range(1, 4):
    books = books + 45
    dvds = dvds + 32
    games = games + 15
    print(f'Month {month}')
    print(f'\tBooks: {books}')
    print(f'\t DVDs: {dvds}')
    print(f'\tGames: {games}')