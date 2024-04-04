def main():
    with open("books/frankenstein.txt", "r") as file:
        text = file.read()

    print("--- Begin report of books/frankenstein.txt ---\n")
    print(f"{word_count(text)} words found in the document")
    print("\n")

    for key in character_count(text):
        print(f"The '{key}' character was found {character_count(text)[key]} times\n")
    print("--- End report ---")

def word_count(text):
    words = text.split()
    return len(words)

def character_count(text):
    char_count = {}

    for word in text:
        letter = word.lower()
        if letter in char_count and letter.isalpha():
            char_count[letter] += 1
        elif letter.isalpha() and letter not in char_count:
            char_count[letter] = 1
        else: 
            pass
        
    char_count = dict(sorted(char_count.items(), key=lambda x: x[1], reverse=True))
    return char_count



if __name__ == "__main__":
    main()