# 
# Alex Cesar Rosa
# 8/21/2024
# This program prompts the user for the filename of a file to analyze.
# It will then output the total number of words, the number of times each
# word appears in the file, and the list of words with that appear the
# most.
#

def read_file(filename):
    """Reads the content of a file and returns it as a string."""
    try: 
        with open(f"{filename}", "r") as file1:
            content = ""
            for line in file1:
                content += line
    except FileNotFoundError:
        print(f"File '{filename}' not found")
        exit()

    return content


def word_count(text):
    """Counts the total number of words in the text."""
    words = text.split()

    return len(words)


def frequency_analysis(text):
    """Analyzes the frequency of each word in the text."""
    words = text.split()
    frequency = {}
    for word in words:
        word = word.lower()
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency


def most_frequent_word(frequency):
    """Identifies the most frequently used word(s) in the text."""
    max_count = max(frequency.values())
    most_frequent = [word for word, count in frequency.items() if count == max_count]
    
    return most_frequent


def main():
    """Main function to run the text file analyzer."""
    filename = input("Enter the name of the file to analyze: ")
    text = read_file(filename)
    if text is not None:
        print("\nAnalyzing text...\n")
        print("Total Word Count:", word_count(text))

        frequency = frequency_analysis(text)
        print("\nWord Frequency Analysis:")
        for word, count in frequency.items():
            print(f"{word}: {count}")

        most_frequent = most_frequent_word(frequency)
        print("\nMost Frequent Word(s):", ', '.join(most_frequent))


if __name__ == "__main__":
    main()
