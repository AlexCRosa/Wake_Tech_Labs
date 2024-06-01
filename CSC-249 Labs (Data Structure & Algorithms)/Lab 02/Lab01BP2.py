#
# Alex Cesar Rosa
# 6/4/2024
#

def main():
    kwh, customer_type = get_user_input()

    energy_charge = bill_calculator(kwh, customer_type)

    print(f"Please pay this amount: ${energy_charge:.2f}")


def get_user_input():
    kwh = int(input("Enter kilowatt hours used: "))
    while kwh < 0:
        print("kWh cannot be negative.")
        kwh = int(input("Enter kilowatt hours used: "))

    customer_type = input("Enter R for residential customer, B for business customer: ").upper()
    while customer_type not in ["R", "B"]:
        customer_type = input("Enter R for residential customer, B for business customer: ").upper()

    return kwh, customer_type


def bill_calculator(kwh, customer_type):
    residential_index = 0.12
    business_index = 0.16

    if customer_type == "R":
        energy_charge = kwh * residential_index
    elif customer_type == "B":
        energy_charge = kwh * business_index

    return energy_charge


if __name__ == '__main__':
    main()
