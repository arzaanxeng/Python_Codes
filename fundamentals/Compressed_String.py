"""
The Compressed String Validator:

Concept: String manipulation and Conditionals.
The Challenge: A simple compression algorithm replaces repeated characters with the character followed by the count
(e.g., "aaaabb" becomes "a4b2"). Write a function that takes a compressed string and returns the original string.
Edge Case: Ensure your code handles counts greater than 9 (e.g., "a12" means 12 'a's, not 'a' once and then the number 2).

"""
import re

def decompress_string(compressed):

    pattern = r"([a-zA-Z])(\d+)"
    matches = re.findall(pattern, compressed)
    result = ""
    for char, count in matches:
        # string combination
        result += char * int(count)

    return result

def main():
    while True:
       compressed_string = input("Enter a compressed string(eg :-> a10b34 ) : ")
       pattern = re.compile(r"([a-zA-Z])(\d+)")
       if pattern.match(compressed_string):
           result = decompress_string(compressed_string)
           print(f"The extended string is : {result}")
           choice =input("Would you like to use the program again?\nPress 'y' to continue and any other key to exit.").lower()
           if choice == "y":
               continue
           else:
               print("Thank you for using this program")
               break
       else:
           print("Invalid format! Please use Letter+Number (e.g., x5y12).")
           continue

if __name__ == "__main__":
    main()





