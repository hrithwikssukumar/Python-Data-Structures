
def process_words(text):
    words = text.split()
    processed_words = sorted(set(words))
    return ' '.join(processed_words)
input_text = input("Enter the text: ")
result =process_words(input_text)
print(f"The arranged text is : {result}")    


#class based method

class TextProcessor:
    def __init__(self, text):
        self.text = text

    def process_words(self):
        words = self.text.split()
        processed_words = sorted(set(words))
        return ' '.join(processed_words)

# User input and result
input_text = input("Enter the text: ")
processor = TextProcessor(input_text)
result = processor.process_words()
print(f"The arranged text is: {result}")

    