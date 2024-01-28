def morse_translator(text):
    # Define the Morse code dictionary
    morse_code_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',
    }

    # Initialize the result string
    result = []

    # Split the input text into words
    words = text.split()

    for word in words:
        # Translate each character to Morse code and join them with space
        morse_word = ' '.join(morse_code_dict.get(char.upper(), char) for char in word)

        # Append the Morse code for the word to the result
        result.append(morse_word)

    # Join the Morse code for each word with a forward slash
    morse_text = '/'.join(result)

    return morse_text

# Example usage:
input_text = "Hello World"
result = morse_translator(input_text)
print(result)
