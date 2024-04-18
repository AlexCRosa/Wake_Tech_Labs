#
# Alex Cesar Rosa
# 4/21/2024
# ITS Python Certification Review - Problem 1 (string format method)
#
TAX_RATE = 0.07

def main():
    title = 'From Here to Python'
    price = 4.50
    count = 7

    # TODO: Convert these 4 output statements so they are using f-strings
    #  instead of the string format method
    # print('We have {0} copies of the book.'.format(count))
    # Comment the above line and put your conversion on the next line
    print(f"We have {count} copies of the book.")
    # print('The {0} copies cost {1:.2f} each.'.format(count, price))
    # Comment the above line and put your conversion on the next line
    print(f"The {count} copies cost {price:.2f} each.")
    # print('Title: {2}\nCount: {0}\nPrice: {1:.2f}'.format(count, price, title))
    # Comment the above line and put your conversion on the next line
    print(f"Title: {title}\nCount: {count}\nPrice: {price:.2f}")
    # print('The tax on {0:.2f} is {1:.2f}.'.format(price, price * TAX_RATE))
    # Comment the above line and put your conversion on the next line
    print(f"The tax on {price:.2f} is {price * TAX_RATE:.2f}.")

    print()

    # TODO: Convert these 4 output statements so they are using the string
    #  format method instead of f-strings
    # print(f'The title of the book is {title}.')
    # Comment the above line and put your conversion on the next line
    print("The title of the book is {0}.".format(title))
    # print(f'"{title}" costs {price:.2f}')
    # Comment the above line and put your conversion on the next line
    print('"{0}" costs {1:.2f}'.format(title, price))
    # print(f'We have {count} copies of "{title}" in stock.')
    # Comment the above line and put your conversion on the next line
    print('We have {0} copies of "{1}" in stock.'.format(count, title))
    # print(f'To buy all {count} copies of "{title}" will cost {count * price:.2f}')
    # Comment the above line and put your conversion on the next line
    print('To buy all {0} copies of "{1}" will cost {2:.2f}'.format(count, title, count * price))

main()
