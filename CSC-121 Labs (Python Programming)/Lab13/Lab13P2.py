#
# Alex Cesar Rosa
# 4/21/2024
# ITS Python Certification Review - Problem 1 (sys module)
#

import sys
import random


def main():
    print(f"Grabbing {sys.argv[3]} random numbers between {sys.argv[1]} and {sys.argv[2]}:")
    print(random.sample(list(range(int(sys.argv[1]), (int(sys.argv[2]) + 1))), k=int(sys.argv[3])))


main()
