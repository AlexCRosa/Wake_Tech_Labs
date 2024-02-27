#
# Alex Cesar Rosa
# 2/26/2024
# This program was created to test the ability to examine and manipulate strings
#
ip_address = input("Please enter an IP address or 'Q' to quit: ")

while ip_address.upper() != "Q":
    temp_list = ip_address.split(".")
    if len(temp_list) != 4:
        print("Error: An IP address should consist of 4 parts separated by periods.")

        ', '.join(temp_list)