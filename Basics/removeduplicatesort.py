
def process_words(text):
    words = text.split()
    processed_words = sorted(set(words))
    return ' '.join(processed_words)
input_text = input("Enter the text: ")
result =process_words(input_text)
print(f"The arranged text is : {result}")    
    