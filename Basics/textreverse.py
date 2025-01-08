

def text_reverse(text):
    words = text.split()
    reversed_list = []
    for word in words:
        reversed_words = word[::-1]
        reversed_list.append(reversed_words)
        return ' '.join(reversed_list)
text =input("Enter the text: ")
result = text_reverse(text)
print(f"The reversed text is : {result}")   
     
