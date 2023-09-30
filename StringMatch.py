# StringMatch.py

import sys

def brute_force_string_match(text, pattern):
    n = len(text)
    m = len(pattern)
    for i in range(n - m + 1):
        j = 0
        while j < m and text[i + j] == pattern[j]:
            j += 1
        if j == m:
            return i
    return -1

def interactive_mode():
    text = input("Enter the text: ")
    pattern = input("Enter the pattern to search for: ")
    index = brute_force_string_match(text, pattern)
    print("Index of the first occurrence:", index)

def file_mode():
    with open("input.txt", "r") as file:
        num_test_cases = int(file.readline().strip())
        with open("output.txt", "w") as output_file:
            for _ in range(num_test_cases):
                text = file.readline().strip()
                pattern = file.readline().strip()
                index = brute_force_string_match(text, pattern)
                output_file.write(str(index) + "\n")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 StringMatch.py [interactive/file]")
        sys.exit(1)

    mode = sys.argv[1]
    if mode == "interactive":
        interactive_mode()
    elif mode == "file":
        file_mode()
    else:
        print("Invalid mode. Please use 'interactive' or 'file'.")
        sys.exit(1)

