
word = input("Input some word: ")
word = word.lower()

palindrome_check = None

if len(word) % 2 != 0:
    palindrome_check = False
else:
    for i, e in enumerate(word):
        if word[i] != word[len(word)-1-i]:
            palindrome_check = False
            break
        else:
            palindrome_check = True

print(palindrome_check)