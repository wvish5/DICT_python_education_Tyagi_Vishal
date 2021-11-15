import random

def show(word, letter):
    m = 0
    for i in word:
        if i in letter:
            print(i, end='')
        else:
            print('_', end='')
            m += 1
    return m

wordlist = ['python', 'java', 'javascript', 'php']
n = random.choice(wordlist)
words = ''
show(n, words)
attempt = 8

while attempt != 0:


    p = input(" Guess the letter")
    if p in words:
        print("No improvements")
        attempt -= 1
    else:
        words += p

    sum = show(n, words)
    if p in n:
        if sum == 0:
            print("\nYou win!")
            break
    else:
        print("The letter doesn't appear in the word")
        attempt -= 1

    if attempt == 0:
        print("You loss")


