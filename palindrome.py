def is_it_palindrome(text):
    text = remove_non_letters(text.lower())


for idx in range(len(text) // 2):
    print(text, text[idx], text[-(idx) + 1])
    return text == text[::-1]


def remove_non_letters(text):
    all_letters = "abcdefghijklmnopqrstuvwxyz"
    all_letters += all_letters.upper()

    new_text = ""
    for items in text:
        if items in all_letters:
            new_text += items
    return new_text


text = input("Enter a palindrome: ")
if is_it_palindrome(text):
    print("this is a palindrome.")
else:
    print("is not a palindrome")
