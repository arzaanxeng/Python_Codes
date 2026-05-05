"""Objective:
You are a junior developer at a cybersecurity firm called "CipherNet".
Your team has intercepted raw encoded messages from a suspicious
server. Your job is to build a string processing pipeline that
cleans, analyses, decodes, and generates a full intelligence
report from the raw intercepted data.

raw_message = "   hELLo__wORLd__tHIs__Is__a__sECrEt__mEsSaGe__fRoM__cIpHeRnEt   "
cipher_key = {
    "a": "@",
    "e": "3",
    "i": "!",
    "o": "0",
    "u": "^"
}
metadata = "AGENT:Shadow|LEVEL:5|LOCATION:Karachi|STATUS:Active|CLEARANCE:Platinum"

Task 1 — Clean & Normalize
Write a function clean_message(raw_message) that:
Strips leading and trailing whitespace
Replaces all __ with a single space
Converts entire message to lowercase
Returns the cleaned message

Task 2 — Message Analysis
Write a function analyse_message(clean_msg) that:
Counts total number of characters (excluding spaces)
Counts total number of words
Finds the longest word in the message
Finds the most repeated word
Counts how many times each vowel (a, e, i, o, u) appears
Returns all results as a tuple of 5 values


Task 3 — Cipher Encoding
Write a function encode_message(clean_msg, cipher_key) that:
Loops through every character in the message
If the character exists as a key in cipher_key, replace it with the value
Otherwise keep the character as is
Returns the fully encoded message string


Task 4 — Metadata Extractor
Write a function extract_metadata(metadata) that:
Splits the metadata string by |
Then splits each part by : to get key and value
Stores everything in a dictionary
Returns the dictionary

Task 5 — Intelligence Report
Write a function generate_report(clean_msg, analysis, encoded, meta) that:
Unpacks the analysis tuple into 5 variables
Prints the full report exactly like this:

"""


raw_message = "   hELLo__wORLd__tHIs__Is__a__sECrEt__mEsSaGe__fRoM__cIpHeRnEt   "
cipher_key = {
    "a": "@",
    "e": "3",
    "i": "!",
    "o": "0",
    "u": "^"
}
metadata = "AGENT:Shadow|LEVEL:5|LOCATION:Delhi|STATUS:Active|CLEARANCE:Platinum"

def clean_message(raw_message):
    clean_msg = raw_message
    clean_msg = clean_msg.strip()
    clean_msg = clean_msg.lower()
    clean_msg = clean_msg.replace("__", " ")
    return clean_msg

def analyse_message(clean_msg):

    words_count = len(clean_msg.split(" "))

    largest_count_word = ""
    for word in clean_msg.split(" "):
        if len(word) > len(largest_count_word):
            largest_count_word = word

    string = "".join(clean_msg.split(" "))

    words = clean_msg.split(" ")
    most_repeated = max(words, key=words.count)

    letters_count = 0
    for _ in string :
        letters_count += 1

    count_a = 0
    count_e = 0
    count_i = 0
    count_o = 0
    count_u = 0
    for letter in string:
        if letter == "a":
            count_a += 1
        elif letter == "e":
            count_e += 1
        elif letter == "i":
            count_i += 1
        elif letter == "o":
            count_o += 1
        elif letter == "u":
            count_u += 1
    return (letters_count, words_count, largest_count_word, most_repeated,
            f"a={count_a}  e={count_e}  i={count_i}  o={count_o}  u={count_u}")


def encode_message(clean_msg, cipher_key):
    for key , value in cipher_key.items():
        if key in clean_msg:
            clean_msg = clean_msg.replace(key, value)
    updated_string = clean_msg
    return updated_string

def extract_metadata(metadata) :
    metadata = metadata.strip()
    parts = metadata.split("|")
    dictionary = dict()
    for part in parts:
        key , value = part.split(":")
        dictionary[key] = value
    return dictionary

def generate_report(clean_msg, analysis, encoded, meta):
    letters_count, words_count, longest_word, most_repeated, vowels = analysis

    print(f"\n{'═' * 42}")
    print(f"{'CIPHERNET INTELLIGENCE REPORT':^42}")
    print(f"{'═' * 42}")

    print(f"\n--- AGENT METADATA ---")
    for key, value in meta.items():
        print(f"{key:<10} : {value}")

    print(f"\n--- MESSAGE ANALYSIS ---")
    print(f"Clean Message   : {clean_msg}")
    print(f"Total Characters: {letters_count}")
    print(f"Total Words     : {words_count}")
    print(f"Longest Word    : {longest_word}")
    print(f"Most Repeated   : {most_repeated}")
    print(f"Vowel Counts    : {vowels}")

    print(f"\n--- ENCODED MESSAGE ---")
    print(f"{encoded}")

    print(f"\n{'═' * 44}")
    print(f"{'CIPHERNET — CLASSIFIED':^44}")
    print(f"{'═' * 44}")


clean_msg = clean_message(raw_message)
analysis = analyse_message(clean_msg)
encoded = encode_message(clean_msg, cipher_key)
meta = extract_metadata(metadata)
generate_report(clean_msg, analysis, encoded, meta)














