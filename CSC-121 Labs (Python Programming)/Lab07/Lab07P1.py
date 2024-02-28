#
# Alex Cesar Rosa
# 2/26/2024
# This program was created to test the ability to examine and manipulate strings
#
def main():

    ip_address = input("Please enter an IP address or 'Q' to quit: ")

    while ip_address.upper() != "Q":
        temp_list = ip_address.split(".")
        if len(temp_list) != 4:
            print("Error: An IP address should consist of 4 parts separated by periods.")
            ip_address = input("Please enter an IP address or 'Q' to quit: ")
        else:
            for i in range(len(temp_list)):
                if not temp_list[i].isdigit():
                    print(f"Error with {temp_list[i]}: Each part of the IP address should be a number between 0 and 255.")
                    break
                elif int(temp_list[i]) > 255:
                    print(f"Error with {temp_list[i]}: Each part of the IP address should be a number between 0 and 255.")
                    break
            else:
                print(f"Reformatted IP address: {':'.join(temp_list)}")
            ip_address = input("Please enter an IP address or 'Q' to quit: ")


main()
