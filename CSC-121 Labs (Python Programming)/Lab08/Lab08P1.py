#
# Alex Cesar Rosa
# 3/4/2024
# Analyze the messages in the log file to identify any issues
#

def main():
    try:
        file1 = open("program.log", "r")

        critical = 0
        error = 0
        warning = 0
        info = 0
        unknown = 0

        for line in file1:
            temp = line.split()
            if temp[3] == "CRITICAL":
                critical += 1
            elif temp[3] == "ERROR":
                error += 1
            elif temp[3] == "WARNING":
                warning += 1
            elif temp[3] == "INFO":
                info += 1
            else:
                unknown += 1

        print(f"CRITICAL: {critical}")
        print(f"ERROR: {error}")
        print(f"WARNING: {warning}")
        print(f"INFO: {info}")
        print(f"UNKNOWN: {unknown}")
    except FileNotFoundError:
        print("File program.log not found")
    else:
        file1.close()


main()
