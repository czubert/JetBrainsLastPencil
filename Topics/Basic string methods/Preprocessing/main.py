user_input = input()
punctuation_marks = [",", ".", "!", "?"]
for i in punctuation_marks:
    user_input = user_input.replace(i, "")
print(user_input.lower())
