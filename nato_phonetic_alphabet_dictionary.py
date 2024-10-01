# NATO Phonetic Alphabet Dictionary

def main():
    # Step 1: Create the NATO Phonetic Alphabet Dictionary
    nato_alphabet = {
        "A": "Alpha",
        "B": "Bravo",
        "C": "Charlie",
        "D": "Delta",
        "E": "Echo",
        "F": "Foxtrot",
        "G": "Golf",
        "H": "Hotel",
        "I": "India",
        "J": "Juliett",
        "K": "Kilo",
        "L": "Lima",
        "M": "Mike",
        "N": "November",
        "O": "Oscar",
        "P": "Papa",
        "Q": "Quebec",
        "R": "Romeo",
        "S": "Sierra",
        "T": "Tango",
        "U": "Uniform",
        "V": "Victor",
        "W": "Whiskey",
        "X": "X-ray",
        "Y": "Yankee",
        "Z": "Zulu"
    }

    # Step 2: Develop the Spelling Program
    def spell_word():
        # Prompt user for a word
        user_word = input("Enter a word to spell using NATO phonetic alphabet: ")
        # Convert the word to uppercase to match dictionary keys
        user_word = user_word.upper()

        # For each letter in user_word, find the corresponding NATO phonetic term in nato_alphabet
        for letter in user_word:
            if letter in nato_alphabet:
                print(nato_alphabet[letter])
            else:
                print(f"{letter} is not a valid letter.")

    # Step 3: Incorporate a Main Function
    spell_word()

# Step 4: Test Your Program
if __name__ == "__main__":
    main()
